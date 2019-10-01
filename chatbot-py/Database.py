import mysql.connector
try: 
        con = mysql.connector.connect (host="localhost", user="root", password="codio", database="name")
        print("Database was successful")
except:
        print("Some Error")