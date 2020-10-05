from db.item_db import *

def list_items():
    data_list = []
    items = get_all_items()
    for item in items:
        data_dict = {}
        data_dict['id'] = item[0]
        data_dict['name'] = item[1]
        data_dict['price'] = item[2]
        data_list.append(data_dict)
    return data_list
