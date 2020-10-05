import json
from psycopg2.extras import execute_values
from src.db.db_utils import *
from src.db.user_db import insert_user

def insert_json_file():
    execute_sql_file('data/schema.sql')
    with open('data/testUsers.json', "r") as json_file:
        data = json.load(json_file)
    list_of_users = []
    for user in data:
        userRegister = {}
        userRegister["username"] = user["username"]
        userRegister["email"] = user["email"],
        userRegister["password"] = user["password"]
        insert_user(userRegister)
