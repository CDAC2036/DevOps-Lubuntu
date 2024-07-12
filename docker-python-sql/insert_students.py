import mysql.connector
import os
import time

students=[
	('7','Alice','DAI'),
	('8','bob','DESD'),
	('9','Charlie','DAC')
]
mydb=None

try:
	mydb=mysql.connector.connect(
			host='mysql',
			user='root',
			password='chang-me',
			port=3306)

	mycursor=mydb.cursor()
	
	mycursor.execute("CREATE DATABASE IF NOT EXISTS cdac")

	mycursor.execute("USE cdac")

	mycursor.execute("""CREATE TABLE IF NOT EXISTS student(PRN VARCHAR(255) NOT NULL,
								NAME VARCHAR(255) NOT NULL,
								course VARCHAR(255) NOT NULL,
								PRIMARY KEY(PRN))
				""")
	
	sql="INSERT INTO student(PRN,Name,course) VALUES(%s,%s,%s)"
	
	mycursor.executemany(sql, students)
	
	print(f"{mycursor.rowcount} records inserted successfully")

	sql="SELECT * FROM student"
	
	mycursor.execute(sql)
	
	result=mycursor.fetchall()

	for row in result:
		print(row)

except mysql.connector.Error as err:
	print("Error: ",err)


finally:
	if mydb and mydb.is_connected():
		mycursor.close()
		mydb.close()
		print("Connection Closed.")
