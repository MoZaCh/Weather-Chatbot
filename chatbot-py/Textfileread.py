file = open("TextFile.txt","r") #Open specific file and read

#STEP 2
linelist = file.readlines() #Read each line
count = len(linelist) #Break it down each line number

#STEP 3
#print (count)
#input = int(input("display line number:"))
print (linelist[1]) #Choose which line/question to display to user.

file.close() #Close the file 