import json
import requests

from pprint import pprint

with open('mount-data.json') as json_data:
    data = json.load(json_data)

is_flying = []

for mount in data["mounts"]["collected"]:
    if mount["isFlying"]:
        is_flying.append(mount)

for i in is_flying:
    pprint(i["name"])

