import requests
import json


def return_result():
    try:
        wa = "http://127.0.0.1:5000/return_result"
        student_id = int(input("Enter id: "))
        user_type = input("Enter the user type: ").lower()

        data = {
            "id": student_id,
            "type": user_type
        }

        res = requests.post(wa, json=json.dumps(data))
        print(res)
        data = res.json()
        ans = data
        print(ans)

    except Exception as e:
        print(e)


return_result()
