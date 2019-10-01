file = open("TextFile.txt","w") #Opens the chosen text file 

file.write("Your name? ") #Writes the question in the text file
Name = input("Your name? ") 
file.write(Name) #adds the name to the file

file.write("\nHello World")
file.write("\nThis is our new text file") 
file.write("\nand this is another line.") 
file.write("\nWhy? Because we can.") 

file.close()  #Closes the file

file = open("TextFile.txt","r") #Opens the chosen text file 

Readfromfile = file.read() #Reads everything in the file
print(Readfromfile)

file.close() #Closes the file