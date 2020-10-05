import os
from .db_utils import *

def rebuild_tables():
    execute_sql_file('data/schema.sql')

def get_all_users():
    return execute_get_all('SELECT * FROM users;')

def get_num_all_users():
    return execute_get_all('SELECT count(*) FROM users;')
