import requests
import json
import os
import subprocess
import sys

decide = input ("Please decide any one method- GET POST PATCH or DELETE : ")
if decide in "GET":
  exec(open('autoGET.py').read())
  
if decide in "POST":
  exec(open('autoPOST.py').read())
  
if decide in "PATCH":
  exec(open('autoPATCH.py').read())
  
if decide in "DELETE":
  exec(open('autoDELETE.py').read())

