from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlite3 import connect
import json


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student_results.db"
app.config["JSON_SORT_KEYS"] = False
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


@app.route("/return_result", methods=['POST'])
def return_result():
    if request.method == 'GET':
        return jsonify({"msg": "Use 'POST' method for this API."})

    data = json.loads(request.get_json())
    student_id = data["id"]
    user_type = data["type"]

    if user_type.lower() != 'student':
        return jsonify({"msg": "Invalid user type"})

    con = None
    try:
        con = connect('student_results.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM StoreModel WHERE rno = '%d'" % student_id)
        data = cursor.fetchall()

        if not data:
            return jsonify({"msg": "Marks details not uploaded yet."})

        return jsonify(
            {
                "id": data[0][0],
                "phy": data[0][1],
                "chem": data[0][2],
                "maths": data[0][3],
                "eng": data[0][4]
            }
        )

    except Exception as e:
        con.rollback()
        return jsonify({"msg": "There's some issue: " + str(e)})

    finally:
        if con is not None:
            con.close()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
