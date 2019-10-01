# Code by Varun Mamtani.
import requests #Importing the request package to use the function to request data from the Open Weather API website
import json #
import random
  
def getForecast(city, country): #Function for getting the live data forecast
    api_address = 'http://api.openweathermap.org/data/2.5/forecast?appid=ef2bdeaff14f90839f13e823e5c8807b&q=' #Api link/url that will be used to get live data from Open Weather API
    
    
    url = api_address + city + country #api address + the cith and country code 
    json_data = requests.get(url).json() #Get json data from the API page 
   
    formatted_data = json_data['list'][0]['main'] #Extracting the weather description from the API
    formatted_data3 = json_data['list'][0]['weather'][0]['description'] #Extracting the weather description from the API
    formatted_data2 = json_data['list'][0]['main']['temp']  #Extracting the temperature description from the API
    formatted_data4 = json_data['list'][0]['main']['temp_min']
    formatted_data5 = json_data['list'][0]['main']['temp_max']
    formatted_data6 = json_data['list'][0]['clouds']['all']
    
    
    celsius_temp = formatted_data2 - 273.15 #Converting Kelvin to Celsius
    celsius_temp = round(celsius_temp) #round the number
    celsius_min = formatted_data4 -273.15 #Converting Kelvin to Celsius
    celsius_min = round(celsius_min) #round the number
    celsius_max = formatted_data5 -273.15 #Converting Kelvin to Celsius
    celsius_max = round(celsius_max) #round the number
    
    if celsius_temp > 15: #If statements, if temp is more than 15 then execute the block of codes that are indented
        print("City:", city + country)        
        print("Advice: It will be nice and warm in " + city + '.')
        
    elif celsius_temp > 5 and formatted_data == 'Rain': #If statements, if temp is more than 5 and it is raining then execute the block of codes that are indented
        print("City:", city + country)
        print("Advice: It will be chilly outside in " + city + "." + " Please ensure you are equipped with an umbrella.")
        
    elif celsius_temp > 5:
        print("City:", city + country)
        print("Advice: It will be chilly outside in " + city + ".")
    
    else: 
        print("City:", city + country)
        print("Advice: It will be freezing outside in " + city +", a jacket is certainly recommended.")
    
    return "Description: " + formatted_data3 + "\n" + "Clouds: " + str(formatted_data6) + ("%") + ("\n") + ("Temperature: ") + str(celsius_temp) + "°C" + "\n" + "Average: " + str(celsius_min) + " to " + str(celsius_max) + "°C"
    
# when the function is called it will return all the information above. i.e. the temperature, advice, description and the % of cloud.

###Code End