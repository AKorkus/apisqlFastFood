from flask import jsonify, abort, request, render_template, redirect, url_for
from models import meals
from forms import MealForm
from app import app, meal_attr




# NIE API...............................................................................................................
# Menu:
@app.route("/menu/", methods=["GET", "POST"])
def meals_list():
    
    form = MealForm()
    error = ""
    new_id = meals.all()[-1]["id"] + 1

    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            data['id'] = new_id
            meals.create(data)
            #meals.save_all()

        return redirect(url_for("meals_list"))
        

    return render_template("meals.html", form=form, meals=meals.all(), error=error)


# Meal
@app.route("/menu/<int:meal_id>/", methods=["GET", "POST"])
def meal_details(meal_id):

    meal = meals.get(meal_id)
    form = MealForm(data=meal)


    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            data['id'] = meal_id
            meals.update(meal_id, data)

        return redirect(url_for("meals_list"))
    

    return render_template("meal.html", form=form, meal_id=meal_id, meal = meal)



    # API...........................................................................................................................

# Wszystkie:
@app.route("/api/v1/meals/", methods=["GET"])
def meals_list_api_v1():
    return jsonify(meals.all())


@app.route("/api/v1/meals/", methods=["POST"])
def create_meal():
    if not request.json or not 'article' in request.json:
        abort(400)
    meal = {
        'id': meals.all()[-1]['id'] + 1,
        'article': request.json['article'],
        'price': request.json['price']
    }
    for attr in meal_attr:
        meal[attr] = request.json[attr]
    meals.create(meal)
    return jsonify({'meal': meal}), 201


# Pojedyńcze:
@app.route("/api/v1/meals/<int:meal_id>", methods=["GET"])
def get_meal(meal_id):
    meal = meals.get(meal_id)
    if not meal:
        abort(404)
    return jsonify({"meal": meal})


@app.route("/api/v1/meals/<int:meal_id>", methods=['DELETE'])
def delete_meal(meal_id):
    result = meals.delete(meal_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/meals/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):
    meal = meals.get(meal_id)
    if not meal:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'article' in data and not isinstance(data.get('article'), str),
        'form' in data and not isinstance(data.get('form'), str),
        'meat' in data and not isinstance(data.get('meat'), str),
        'salad1' in data and not isinstance(data.get('salad1'), str),
        'salad2' in data and not isinstance(data.get('salad2'), str),
        'sauce' in data and not isinstance(data.get('sauce'), str),
        'price' in data and not isinstance(data.get('price'), float)
    ]):
        abort(400)
    meal = {
        'id': meal_id,
        'article': data.get('article', meal['article']),
        'form': data.get('form', meal['form']),
        'meat': data.get('meat', meal['meat']),
        'salad1': data.get('salad1', meal['salad1']),
        'salad2': data.get('salad2', meal['salad2']),
        'sauce': data.get('sauce', meal['sauce']),
        'price': data.get('price', meal['price'])
    }
    meals.update(meal_id, meal)
    return jsonify({'meal': meal})