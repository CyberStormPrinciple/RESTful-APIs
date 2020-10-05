from db.user_db import *
from db.user import User
from flask_restful import Resource, reqparse


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400
        return insert_user(data)
