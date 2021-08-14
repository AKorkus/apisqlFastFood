from flask import Flask, jsonify, make_response, request
import views
import config
import initiator



app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY
meal_attr = config.meal_attr

if config.initiate_yes_no:
    initiator.initiate()

# ERROR HANDLER.................................................................................................................

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


# RUN...................................................................................................................
if __name__ == "__main__":
    views.app.run(debug=True)


