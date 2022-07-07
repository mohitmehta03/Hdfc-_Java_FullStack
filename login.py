import mysql.connector
from datetime import date
def get_student_detail():
    try:
        connection = mysql.connector.connect(host='localhost',database='mohit',user='root', password='0706')
        cursor = connection.cursor()
 
        sql_select_query = "select * from students where username= %s"
        cursor.execute(sql_select_query, ( user,))
        record = cursor.fetchall()
        for row in record:
            if user==row[5] and passw==row[6]:
                    print( row[1])
                    print("gender = ", row[4])
                    print("branch=",row[2])
                    print("birthdate = ", row[3])

            else:
                user_=input("Enter username:")
                passw_=input("enter your password:")
                while user_==row[5] and passw_==row[6]:
                    print("Name = ", row[1])
                    print("gender = ", row[4])
                    print("branch=",row[2])
                    print("birthdate = ", row[3])
                break 

                
                get_student_detail()
    except mysql.connector.Error as error:
                            print("Failed to get record from MySQL table: {}".format(error))            
user=input("Enter username:")
passw=input("enter your password:")
get_student_detail()