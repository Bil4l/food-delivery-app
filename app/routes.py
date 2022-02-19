from flask import jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

@app.route('/restaurant')
def restaurant():
    return jsonify({"bonjour":1})
