import sqlite3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlite3 import connect
import json

from sqlalchemy.orm import session
# from app import app
# from app import routes, models


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student_results.db"
db = SQLAlchemy(app)
CORS(app)

# schema definition


class StudentLoginModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(10))
    student = db.Column(db.String(10))
    faculty = db.Column(db.String(10))

    def __init__(self, id, password, student, faculty):
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

    def __init__(self, rno, phy, chem, maths, eng):
        self.rno = rno
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.eng = eng


@app.route("/")
def index():
    return "Hello From Flask Here"


@app.route("/check", methods=["POST", "GET"])
def check():

    data = json.loads(request.get_json())
    id = data["id"]
    password = data["password"]
    con = None
    try:
        con = connect("student_results.db")
        cursor = con.cursor()
        cursor.execute(
            "insert into StudentLoginModel (id, password) values ('%d','%s')"
            % (id, password)
        )
        con.commit()
        return jsonify({"msg": "Details are successfully stored in the database..!"})

    except Exception as e:
        con.rollback()
        return jsonify({"msg": "There's some issue: " + str(e)})

    finally:
        if con is not None:
            con.close()


@app.route("/addresult", methods=["POST", "GET"])
def addresult():
    data = json.loads(request.get_json())
    facultyid = data["facultyid"]
    type = data["type"]
    studentid = data["studentid"]
    physicsmarks = data["physicsmarks"]
    chemmarks = data["chemmarks"]
    mathsmarks = data["mathsmarks"]
    englishmarks = data["englishmarks"]
    con = None
    try:
        con = connect("student_results.db")
        cursor = con.cursor()
        if type != "faculty" and facultyid > 0:
            return jsonify({"msg": "Access Denied"})
        cursor.execute(
            "Insert into StoreModel (rno, phy, chem, maths, eng) values ('%d','%d','%d','%d','%d')" % (studentid, physicsmarks, chemmarks, mathsmarks, englishmarks)
        )
        con.commit()
        return jsonify({"msg": "Details are successfully stored in the database..!"})
    except Exception as e:
        con.rollback()
        return jsonify({"msg": "There's some issue: " + str(e)})
    finally:
        if con is not None:
            con.close()


@app.route('/login',methods=["POST","GET"])
def login():
    r=""
    msg=""
    
    # data = json.loads(request.get_json())
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        # print(data["username"])
        # username=1
        # password="1234"
        conn=sqlite3.connect("student_results.db")
        c=conn.cursor()
        
        c.execute("SELECT * FROM  StudentLoginModel WHERE id='"+username+"' and password='"+password+"'")
        r=c.fetchall()

        for i in r:
            if(username==i[0] and 'password'==i[1]):
                session["logedin"]=True
                session["username"]=username
                return r;
            else:
                return "Invalid username and password"
    else:
        return "Please fill the complete form"


       

    




if __name__ == "__main__":
    app.run(debug=True, port=5000)
