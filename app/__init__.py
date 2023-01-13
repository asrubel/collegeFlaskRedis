from flask import Flask, request
from app.datastorage import init, add_key, get_key, get_all_keys

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask with Redis demo.'


@app.route('/college/redis/init')
def init_datastorage():
    init()
    return 'Datastorage is initialized!'


@app.route('/college/redis/add')
def add_to_datastorage():
    key = request.args.get('key', default='Some key')
    value = request.args.get('value', default='Default value')
    add_key(key, value)
    return 'Key-value pair is added!'


@app.route('/college/redis/get')
def get_from_datastorage():
    key = request.args.get('key', default='Course')
    return get_key(key)


@app.route('/college/redis/get_all')
def load_json():
    return get_all_keys()
