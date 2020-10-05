import os
from .db_utils import *

def rebuild_items_table():
    execute_sql_file('data/schema.sql')

def get_all_items():
    return execute_get_all('SELECT * FROM items;')

def get_num_all_items():
    return execute_get_all('SELECT count(*) FROM items;')

def insert_item(name, price):
    execute_commit('''
        INSERT INTO items (name, price)
            VALUES (%s, %s)
        ''', (name, price))

def update_item(name, price):
    return execute_commit('''
        UPDATE items
            SET price = %s
            WHERE name = %s;
        ''', (price, name))

def remove_item(name):
    return execute_commit('''
        DELETE FROM items
            WHERE name = %s;
        ''', (name,))
