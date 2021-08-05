from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


app = Flask(__name__)

db = SQLAlchemy(app)

class LoginModel(db.Model):
    rno = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(10))

    def __init__(self,rno,password):
        self.rno = rno
        self.password = password

class StoreModel(db.Model):
    rno = db.Column(db.Integer, primary_key=True)
    phy = db.Column(db.Integer, positive=True)
    chem = db.Column(db.Integer,positive=True)
    maths = db.Column(db.Integer,positive=True)
    eng = db.Column(db.Integer,positive=True)

    def __init__(self,phy,chem,maths,eng):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.eng = eng
    



@app.route('/')
def index():
    return "Hello From Flask Here"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

