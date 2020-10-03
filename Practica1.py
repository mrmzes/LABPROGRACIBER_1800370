import requests
import json

output = []

api = str(input("Ingresa su API (OpenWeatherMap): "))

req1 = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid="+api)
req2 = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Paris&appid="+api)
req3 = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Toronto&appid="+api)

x = (json.loads(req1.content))
y = (json.loads(req2.content))
z = (json.loads(req3.content))

output.append(json.dumps(x, indent=4, sort_keys=True))
output.append(json.dumps(y, indent=4, sort_keys=True))
output.append(json.dumps(z, indent=4, sort_keys=True))

print(output[0])
print(output[1])
print(output[2])