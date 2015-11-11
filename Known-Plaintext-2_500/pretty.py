from pprint import *
import json

with open("all.json") as f:
    data = json.load(f)

pprint(data)
