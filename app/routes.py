from flask import jsonify
from app import app

@app.route('/')
def index():
    return "Hello world"

@app.route('/customers')
def customers():
    return jsonify({"id":12}) 