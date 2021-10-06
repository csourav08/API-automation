import requests
import json
import pprint


url='https://gorest.co.in/public/v1/users/'
token = input("Enter your acess token (copy/type the word 'Bearer' without quotes give a space and paste/type acess-token ): ")
ID = input ("Enter the ID of the record you want to update: ")
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

response = requests.request('PATCH', url+ID, data=payload, headers=headers)
pprint.pprint(response.json())
