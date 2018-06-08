import json
import requests

from pprint import pprint

with open('mount-data.json') as json_data:
    data = json.load(json_data)

for item in data.items():
    pprint(item)

