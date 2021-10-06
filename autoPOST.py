import requests
import json
import pprint

# status = 0
url='https://gorest.co.in/public/v1/users'
token = input("Enter your acess token (copy/type the word 'Bearer' without quotes give a space and paste/type acess-token ): ")
name = input ("Enter full name: ")
status = input("Enter status: ")
gender = input("Enter gender: ")
email = input("Enter email: ")


payload = json.dumps({
    'name': name,
    'gender': gender,
    'email': email,
    'status': status
    }
)

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': token
}

response = requests.request('POST', url, data=payload, headers=headers)
pprint.pprint(response.json())