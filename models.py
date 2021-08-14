import inputs
import sql_kommands as sk
import sql_executor as se
from json_handler import tuple_list_to_json_list 


class Meals:

    def all(self):
        columns = []
        for attr in inputs.meals_input:
            columns.append(attr)
        try:
            conn = se.create_connection(r"MexicanFastFood.db")
            query = sk.simple_select("meals")
            touples = se.selektor(conn, query)
            meals = tuple_list_to_json_list(columns, touples)
        except:
            meals = []
        return meals

    def get(self, id):
        meal = [meal for meal in self.all() if meal['id'] == id]
        if meal:
            return meal[0]
        return []

    def create(self, data):
        if "csrf_token" in data:
            data.pop("csrf_token")
        conn = se.create_connection(r"MexicanFastFood.db")
        query = sk.insert_into("meals", data)
        se.execute_sql(conn, query)
        conn.close

    def update(self, id, data):
        meal = self.get(id)
        if "csrf_token" in data:
            data.pop("csrf_token")
        if meal:
            conn = se.create_connection(r"MexicanFastFood.db")
            query = sk.update_by_id("meals", id, data)
            se.execute_sql(conn, query)
            conn.close
            return True
        return False

    def delete(self, id):
        meal = self.get(id)
        if meal:
            conn = se.create_connection(r"MexicanFastFood.db")
            query = sk.delete("meals", id)
            se.execute_sql(conn, query)
            conn.close
            return True
        return False


meals = Meals()
