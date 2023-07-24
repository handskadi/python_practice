import json

data = {"name" : "KADI", "age": 35, "city": "Marrakech"}

with open('data.json', 'w') as file:
    json.dump(data, file)
