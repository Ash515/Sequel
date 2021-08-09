from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from sqlite3 import *
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///student_results.db"
db = SQLAlchemy(app)


class StudentLoginModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(10))
    student = db.Column(db.String(10))
    faculty = db.Column(db.String(10))
   

    def __init__(self,id,password,student,faculty):
        self.id = id
        self.password = password
        self.student = student
        self.faculty = faculty

        


class StoreModel(db.Model):
    rno = db.Column(db.Integer, primary_key=True)
    phy = db.Column(db.Integer)
    chem = db.Column(db.Integer)
    maths = db.Column(db.Integer)
    eng = db.Column(db.Integer)

    def __init__(self,phy,chem,maths,eng):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.eng = eng
    



@app.route('/')
def index():
    return "Hello From Flask Here"

@app.route('/check', methods=['POST','GET'])
def check():
    
    data = json.loads(request.get_json())
    id = data['id']
    password = data['password']
    con = None
    try:
        con = connect('student_results.db')
        cursor = con.cursor()
        cursor.execute("insert into StudentLoginModel (id, password) values ('%d','%s')" % (id,password))
        con.commit()
        return jsonify({'msg': "Details are successfully stored in the database..!"})

    except Exception as e:
        con.rollback()
        return jsonify({'msg': "There's some issue: " + str(e)})
    
    finally:
	    if con is not None:
		    con.close()

	
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

