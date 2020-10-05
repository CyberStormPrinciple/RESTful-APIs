import psycopg2
from .user_db import *
from .db_utils import *

class User:
    def __init__(self, _id, username, email, password):
        self.id = _id
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        user_row = execute_get_one('''
            SELECT * FROM users
                WHERE email = %s
            ''', (email,))
        return validUserRow(cls, user_row)

    @classmethod
    def find_by_id(cls, id):
        user_row = execute_get_one('''
            SELECT * FROM users
                WHERE id = %s
            ''', (id,))
        return validUserRow(cls, user_row)

    @classmethod
    def validUserRow(cls, user_row):
        if user_row:
            user = cls(*user_row)
        # *user_row same as user_row[0], user_row[1], user_row[2], user_row[3]
        else:
            user = None
        return user
