from flask import Flask

app = Flask(__nama__)

stores = [
    {
        'name': 'Hugo Boss'
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/store')
def get_stores():    
    return jsonify({'stores':stores})    

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/stone', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass
