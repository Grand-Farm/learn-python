import requests

response = requests.get("https://api.agify.io?name=meelad")
json = response.json()
print(json)
print("name:", json['name'], "age:", json['age'], "count: ", json["count"])