import json

import requests

responce_API = requests.get("https://dummy.restapiexample.com/api/v1/employees")

data = responce_API.text
parse_json = json.loads(data)

print("Todos:", parse_json)