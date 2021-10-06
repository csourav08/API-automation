import requests
import json
import pprint


url='https://gorest.co.in/public/v1/users/'
token = input("Enter your acess token (copy/type the word 'Bearer' without quotes give a space and paste/type acess-token ): ")
ID = input ("Enter the ID of the record you want to delete: ")

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': token
}

response = requests.request('DELETE', url+ID, headers=headers)
print("record deleted")
