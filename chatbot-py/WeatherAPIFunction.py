###Code Start by Mohammed Zahed Choudhury and logic done by Laurentiu Fleancu

import requests #Importing the request package to use the function to request data/url from the Open Weather API website
import json #Import the json package to decode json data from the API url
import random #import the random function

def readName(name): #function to check if name entered is saved in the text file
    """Reads from a text file"""
    file = open("TextFile.txt","r") #Opens the chosen text file 
    linelist = file.readlines() #Read each line
    namelist = [x.strip("\n") for x in linelist] #Removes the new lines from the text file 
    
    if name in namelist: #If the name entered is already saved in the text file print the message below
        print("Greetings " + name + ", Looks like you've been here before. How may I the Weather Wizard assist you today?")
        
    else: #If the name entered is not in the text file print message below and write name into text file
        print("Welcome " + name + ", Looks like you are new here...Well I am the Weather Wizard and I can assist you with the weather!")
        writeintofile(name)
        
    file.close() #Close the file 
    
    return namelist #Returns the chosen question 
pass #Closes the function


#the first function is used to input data into the textfile 
def writeintofile(write):
    """Input value/variable then saves it into a text file"""
    file = open("TextFile.txt","a") #Opens the chosen text file and appends

    file.write(write) #Writes the question in the text file
    file.write("\n")  #Adds a new line so the next input can be in a new line
    
    file.close()  #Closes the file
    
    return 
pass #Closes the function 


#the second function is used to extract data from the text file
def readfileGreetings():
    """Reads from a text file"""
    file = open("Greetings.txt","r") #Opens the chosen text file 

    linelist = file.readlines() #Read each line
    #count = len(linelist) #Break it down each line number

    #question = linelist[number] #Choose which line/question to display to user.
    question =random.choice(linelist[0:]) #it will choose a random greeting from the text file
    strquestion = question.rstrip('\n') #Removes any blank lines at the end of the line.
    
   
    file.close() #Close the file 
    
    return strquestion #Returns the chosen question 
pass #Closes the function 

# Added random Goodbye generator so it won't be repetitive Laurentiu Fleancu 
def readfileBye():
    """Reads from a text file"""
    file = open("Bye.txt","r") #Opens the chosen text file 

    linelist = file.readlines() #Read each line
    #count = len(linelist) #Break it down each line number

    #question = linelist[number] #Choose which line/question to display to user.
    question =random.choice(linelist[0:8]) #it will choose a random bye from the text file
    strquestion = question.rstrip('\n') #Removes any blank lines at the end of the line.
    
   
    file.close() #Close the file 
    
    return strquestion #Returns the chosen question 
pass #Closes the function 
###Code Edit by Laurentiu Fleancu 

 
def getWeather(city, country): #Function for getting the live data weather
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=ef2bdeaff14f90839f13e823e5c8807b&q=' #Api link/url that will be used to get live data from Open Weather API
    
    
    url = api_address + city + country #api address + the cith and country code 
    json_data = requests.get(url).json() #decode JSON strings into Python


    formatted_data = json_data['weather'][0]['main'] #Extracting the weather description from the API #### Line of code support by Laurentiu Fleancu
    formatted_data3 = json_data['weather'][0]['description'] #Extracting the weather description from the API #### Line of code support by Laurentiu Fleancu
    formatted_data2 = json_data['main']['temp']  # Added by Laur ->Extracting the temperature description from the API #### Line of code support by Laurentiu Fleancu
    formatted_data4 = json_data['main']['temp_min'] #json decodes and provides the min temperature
    formatted_data5 = json_data['main']['temp_max'] #json decodes and provides the max temperature
    formatted_data6 = json_data['clouds']['all'] #json decodes and provides percentage of cloud
    
    # Kelvin to Celsius Converter Created by Laurentiu FLeancu
    celsius_temp = formatted_data2 - 273.15 #Converting Kelvin to Celsius 
    celsius_temp = round(celsius_temp) #round the number 
    celsius_min = formatted_data4 -273.15 #Converting Kelvin to Celsius 
    celsius_min = round(celsius_min) #round the number
    celsius_max = formatted_data5 -273.15 #Converting Kelvin to Celsius
    celsius_max = round(celsius_max) #round the number
    ###Code End by Laurentiu Fleancueancu 
    
    if celsius_temp > 15: #If statements, if temp is more than 15 then execute the block of codes that are indented
        print("City:", city + country)        
        print("Advice: The gods were nice it's warm in" + city + '.')
        
    elif celsius_temp > 5 and formatted_data == 'Rain': #If statements, if temp is more than 5 and it is raining then execute the block of codes that are indented
        print("City:", city + country)
        print("Advice: It is chilly outside in " + city + "." + " Please ensure you are equipped with an umbrella.")
        
    elif celsius_temp > 5:
        print("City:", city + country)
        print("Advice: It is chilly outside in " + city + "."+" Make sure you take a jacket.")
    
    else: 
        print("City:", city + country)
        print("Advice: It is freezing outside in " + city +", a jacket is certainly recommended but it may not be enaugh.")
    
    return "Description: " + formatted_data + ", " + formatted_data3 + "\n" + "Clouds: " + str(formatted_data6) + ("%") + ("\n") + ("Temperature: ") + str(celsius_temp) + "°C" + "\n" + "Average: " + str(celsius_min) + " to " + str(celsius_max) + "°C"
# when the function is called it will return all the information above. i.e. the temperature, advice, description and the % of cloud.

###Code End By Mohammed Zahed Choudhury 