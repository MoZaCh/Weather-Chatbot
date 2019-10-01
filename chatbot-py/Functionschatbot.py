###Code Start by Mohammed Zahed Choudhury

import random #import the random function

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
def readfile():
    """Reads from a text file"""
    file = open("Greetings.txt","r") #Opens the chosen text file 

    linelist = file.readlines() #Read each line
    #count = len(linelist) #Break it down each line number

    #question = linelist[number] #Choose which line/question to display to user.
    question =random.choice(linelist) #it will choose a random greeting from the text file
    strquestion = question.rstrip('\n') #Removes any blank lines at the end of the line.
    
   
    file.close() #Close the file 
    
    return strquestion #Returns the chosen question 
pass #Closes the function 

###Code End 


