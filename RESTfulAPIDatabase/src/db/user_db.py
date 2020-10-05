import os
from .db_utils import *

def rebuild_users_table():
    execute_sql_file('data/schema.sql')

def get_all_users():
    return execute_get_all('SELECT * FROM users;')

def get_num_all_users():
    return execute_get_all('SELECT count(*) FROM users;')

def insert_user(parser_data):
    execute_commit('''
        INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
        ''', (parser_data['username'],
              parser_data['email'],
              parser_data['password']))

def update_user(username, email):
    return execute_commit('''
        UPDATE users
            SET username = %s,
                email = %s,
                password = %s
            WHERE name = %s AND email = %s;
        ''', (username, email, password, username, email))

def remove_user(name):
    return execute_commit('''
        DELETE FROM users
            WHERE name = %s;
        ''', (name,))
