from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello From Flask Here"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

