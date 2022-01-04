import requests
import json


def result():
    try:
        wa = " http://127.0.0.1:5000/addresult"
        facultyid = int(input("Enter faculty id: "))
        type = input("Enter the type: ")
        type = type.lower()
        studentid = int(input("Enter student id/ roll no: "))
        physicsmarks = int(input("Enter physics marks: "))
        chemmarks = int(input("Enter chemistry marks: "))
        mathsmarks = int(input("Enter maths marks: "))
        englishmarks = int(input("Enter english marks: "))
        data = {
            "facultyid": facultyid,
            "type": type,
            "studentid": studentid,
            "physicsmarks": physicsmarks,
            "chemmarks": chemmarks,
            "mathsmarks": mathsmarks,
            "englishmarks": englishmarks,
        }
        res = requests.post(wa, json=json.dumps(data))
        print(res)
        data = res.json()
        ans = data["msg"]
        print(ans)

    except Exception as e:
        print(e)


result()
