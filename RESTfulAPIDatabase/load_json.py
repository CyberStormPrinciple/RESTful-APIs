import json
from psycopg2.extras import execute_values
from src.db.db_utils import *

def insert_json_file():
    execute_sql_file('data/schema.sql')
    with open('data/testUsers.json', "r") as json_file:
        data = json.load(json_file)
    list_of_tuples = []
    for user in data:
        list_of_tuples.append((
            user["id"],
            user["username"],
            user["email"],
            user["password"]))
    connection = connect()
    cursor = connection.cursor()
    sql = "INSERT INTO users(id, username, email, password) VALUES %s"
    execute_values(cursor, sql, list_of_tuples)
    connection.commit()
    connection.close()
