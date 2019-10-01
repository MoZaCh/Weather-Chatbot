import requests
import json

#city = input("")
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=ef2bdeaff14f90839f13e823e5c8807b&q='

city = "Manchester"
#city = input("")

url = api_address + city

json_data = requests.get(url).json()

formatted_data = json_data['weather'][0]['main']
formatted_data2 = json_data['main']['temp']
celsius_temp = formatted_data2 - 273.15

print(city + ":")
print(formatted_data)
print((round(celsius_temp,0)), "Degrees")