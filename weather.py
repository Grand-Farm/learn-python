from urllib import request
import requests

api_key = "need api key"
city = "fargo"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+" "

request = requests.get(url)
json = request.json()
print(json)
