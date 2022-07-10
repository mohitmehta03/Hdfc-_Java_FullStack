import datetime
import mysql.connector
def insert_students_detail():
        #establishing the connection
        connection = mysql.connector.connect( host='localhost',user='root', password='0706', database='mohit')

        #Creating a cursor object using the cursor() method
        cursor = connection.cursor()
        insert=("INSERT INTO students(name_,branch,birthday,Gender,username,password)VALUES (%s, %s, %s, %s, %s, %s)")
        # Executing the SQL command
        cursor.execute(insert,(N, S, O, P, Q, R))
        connection.commit ()
        connection.close()
# Closing the connection                       
N=input("Enter your name:") 
y = int(input("Enter your birth year:"))
m =int(input("Enter your birth month:"))
d=int(input("Enter your birthdate:"))
O=datetime.date(y,m,d)
P=input("Enter your gender :")
Q=input("Enter your Username for account :")
R=input("Enter password:")
S=input("enter your branch :")
insert_students_detail()
print("vs ydv")
