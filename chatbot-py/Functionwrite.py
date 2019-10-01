name = input("Your name: ")



def writeintofile(write):
    """Input value then saves it into a text file"""
    file = open("TextFile.txt","a") #Opens the chosen text file 

    file.write(write + "\n") #Writes the question in the text file
    
    file.close()  #Closes the file
    
    return 
pass #Closes the function 


writeintofile(name) #Calls the function with variable name given a value