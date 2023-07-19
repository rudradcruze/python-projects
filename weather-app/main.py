import requests
import json

city = input("Please enter the city to get weather: ")

url = f"http://api.weatherapi.com/v1/current.json?key=9f805cfaa4574a3e8fc115247231907&q={city}"

r = requests.get(url)
weather = json.loads(r.text)

for k, v in weather.items():
  for ik, iv in v.items():
      print(ik, iv)
