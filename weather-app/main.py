import requests
import json
import os


def speak(command):
    print(command)
    os.system(f'''mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{command}"")(window.close)")''')


speak("Weather Speak App. Created By Francis Rudra D Cruze")
city = input("Please enter the city to get weather: ")
command = f"The weather status of {city}"
speak(command)

url = f"https://api.weatherapi.com/v1/current.json?key=9f805cfaa4574a3e8fc115247231907&q={city}"

r = requests.get(url)
weather = json.loads(r.text)

for k, v in weather.items():
    command = f"{k} Information"
    speak(command)
    for ik, iv in v.items():
        command = f"{ik} is {iv}"
        speak(command)