import mysql.connector
mydb =  mysql.connector.connect(host= "localhost", user = "root",passwd = "Rohit@2003", database = "movies")
mycursor = mydb.cursor()
mycursor.execute("insert into movies (name,actor,actress,director,year_of_release) values ('KGF','Yash','srinidhi_shetty','Prashanth_neel', 2018)" )
mycursor.execute("insert into movies (name,actor,actress,director,year_of_release) values ('F9','Vin_Diesel','Michelle_Rodriguez','Justin_Lin', 2021)" )
mycursor.execute("insert into movies (name,actor,actress,director,year_of_release) values ('3_Idiots','Amir_Khan','Kareena_Kapoor','Rajkumar_Hirani', 2009)" )
mycursor.execute("insert into movies (name,actor,actress,director,year_of_release) values ('War','Hritik_Roshan','Vaani-Kapoor','Siddharth_Anand', 2019)")
mycursor.execute("insert into movies (name,actor,actress,director,year_of_release) values ('Mission_Kashmir','Hritik_Roshan','Preity_Zinta','Vidhu_Vinod_Chopra', 2000)" )
mydb.commit()