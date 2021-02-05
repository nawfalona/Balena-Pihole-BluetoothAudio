import json
import requests

response = requests.get

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("")

if response.status_code==200:
    jprint(response.json())
else:
    print("red led blink!")


