from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db.item_db import *
from .utils import list_items


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        items = list_items()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {'item': item}
        return {'message': 'Item not found'}, 404

    def post(self, name):
        items = list_items()
        if next(filter(lambda x: x['name'] == name, items), None):
            return {
            'message': "An item with name '{}' already exists.".format(name)
            }, 400
        data = Item.parser.parse_args()
        item = {'name':name, 'price':data['price']}
        try:
            self.insert_item(item['name'], item['price'])
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return item, 201

    def delete(self, name):
        remove_item(name)
        return {'message': 'Item {} deleted'.format(name)}

    def put(self, name):
        items = list_items()
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            try:
                self.insert_item(item['name'], item['price'])
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            item = {'name': name, 'price': data['price']}
            try:
                self.update_item(item['name'], data['price'])
            except:
                return {"message": "An error occurred updating the item."}, 500
        return item

class ItemList(Resource):
    def get(self):
        items = list_items()
        return {'items': items}
