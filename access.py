import mysql.connector
mydb =  mysql.connector.connect(host= "localhost", user = "root",passwd = "Rohit@2003", database = "movies")
mycursor = mydb.cursor()
# to access the whole table
mycursor.execute("select * from movies")
for i in mycursor:
    print(i)

# to access table by actor
'''mycursor.execute("select * from movies where actor = <actor name>")
for i in mycursor:
    print(i)'''