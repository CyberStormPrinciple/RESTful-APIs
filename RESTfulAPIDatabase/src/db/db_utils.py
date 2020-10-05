import psycopg2
import yaml
import os

def connect():
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__), '../../config/db.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])

def execute_sql_file(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    connection = connect()
    cursor = connection.cursor()
    with open(full_path, "r") as file:
        cursor.execute(file.read())
    connection.commit()
    connection.close()

def execute_get_all(sql, args={}):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql, args)
    list_of_tuples = cursor.fetchall()
    connection.close()
    return list_of_tuples

def execute_get_one(sql, args={}):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql, args)
    single_tuple = cursor.fetchone()
    connection.close()
    return single_tuple

def execute_commit(sql, args={}):
    connection = connect()
    cursor = connection.cursor()
    result = cursor.execute(sql, args)
    connection.commit()
    connection.close()
    return result
