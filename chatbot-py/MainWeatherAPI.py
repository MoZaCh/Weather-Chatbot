# Code by Mohammed Zahed Choudhury.

import WeatherAPIFunction #Importing the Weather API function taht i have created
import ForecastAPIFunction

file = open("TextFile.txt","a") #If the textfile.txt does not exist it will create one 
file.close() #Closes the file

print(WeatherAPIFunction.readfileGreetings())#Here i am using the function that i have imported so it displays a random greeting.
name = input() #User enters their name
WeatherAPIFunction.readName(name) #Calls the readName function from WeatherAPI Function


while True: #Repeats the block of code below until user enters no which exits the program.
    city = input("Please enter a city: ")
    country = input("Please specify US, UK, ES(Spain), DE(Germany), FR(France), Romania(RO) AE(Dubai), BD(Bangladesh), IN(India), PK(Pakistan): ")
    country = ',' + country

   
    try: #Prints the statement below if there are not errors
        print(WeatherAPIFunction.getWeather(city, country)) # Prints the live weather data that has been extracted
        forecastInput = input("Would you like to see the forecast for tomorrow (*Yes* or *No*)? ") #Asks the user whether they want to view the forecast for tomorrow ### Line Code by Varun Mamtani.
         
        if forecastInput == 'yes' or forecastInput == 'Yes' or forecastInput == 'YES': # if user enters no the program exits other shows data ### Line Code by Varun Mamtani.
              print(ForecastAPIFunction.getForecast(city, country)) ### Line Code by Varun Mamtani.
              restart = input("Would you like to enter another city (*Yes* or *No*)? ")
        elif forecastInput == 'no' or forecastInput == 'No' or forecastInput == 'NO': ### Line Code by Varun Mamtani.
               restart = input("Would you like to enter another city (*Yes* or *No*)? ") ### Line Code by Varun Mamtani.  
        if restart == 'no' or restart == 'No' or restart == 'NO':
              print(WeatherAPIFunction.readfileBye()+"! " +name+ ", I hope I have been helpful.")
              break
           
             
    except KeyError: #Prints the statement below if there is an KeyError
        print("Sorry, " + name + " I didn't understand that.")
        restart = input("Would you like to try again (*Yes* or *No*)? ") #Asks the user whether they want to try again or not
        if restart == 'no' or restart == 'No' or restart == 'NO': # if user enters no the program exits
            print(WeatherAPIFunction.readfileBye()+"! " +name+ ", I hope I have been helpful.")
            break

####Code End by Mohammed Zahed Choudhury

