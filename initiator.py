import sql_executor as se
import sql_kommands as sk
import json_handler as jh
import inputs

def initiate():
    # Create database:
    conn = se.create_connection(r"MexicanFastFood.db")
    query = sk.create_table("meals", inputs.meals_input, auto_id=False)
    se.execute_sql(conn, query)
    # Fill with initial values:
    menu = jh.read_json("meals.json")
    for meal in menu:
        query = sk.insert_into("meals", meal)
        se.execute_sql(conn, query)
    conn.close

if __name__ == "__main__":
    initiate()