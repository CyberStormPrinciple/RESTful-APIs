import psycopg2
from .user_db import *
from .db_utils import *

class Item:
    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price

    @classmethod
    def find_by_id(cls, id):
        user_row = execute_get_one('''
            SELECT * FROM items
                WHERE id = %s
            ''', (id,))
        return validUserRow(cls, user_row)

    @classmethod
    def find_by_name(cls, name):
        user_row = execute_get_one('''
            SELECT * FROM items
                WHERE name = %s
            ''', (name,))
        return validUserRow(cls, user_row)

    @classmethod
    def validUserRow(cls, user_row):
        if item_row:
            item = cls(*item_row)
        # *user_row same as user_row[0], user_row[1], user_row[2], user_row[3]
        else:
            item = None
        return item
