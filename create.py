#!/usr/bin/env python
#Created by James Vanaselja
#create.py
import RPi.GPIO as GPIO
import SimpleMFRC522
import sys
import signal
import mysql.connector as mariadb
import re
import secrets

def create():
	fetchResults()
	mariadb_connection = mariadb.connect(user=secrets.user, password=secrets.password, database=secrets.database)
	cursor = mariadb_connection.cursor(buffered=True)
	reader = SimpleMFRC522.SimpleMFRC522()
	print("Place card onto Scanner")
	try:
		id, text = reader.read()
		UID = str(id)
#sanitize input by removing non numbers
		re.sub("[^0-9]","",UID)
	
	except:
		print("An error has occured")
	finally:
		GPIO.cleanup()
		
	first_name = str(raw_input("Please type the first name you wish to enter \n"))
	last_name = str(raw_input("Please type the last name you wish to enter: \n"))
	query=("INSERT INTO person ""(LastName,FirstName,UID)" "VALUES(%s, %s, %s);")
	cursor.execute(query,[last_name,first_name,UID])
	mariadb_connection.commit()
	fetchResults()
	cursor.close()
	mariadb_connection.close()


	

def fetchResults():
	mariadb_connection = mariadb.connect(user=secrets.user, password=secrets.password, database=secrets.password)
	cur = mariadb_connection.cursor(buffered=True)
	result_query = ("SELECT * FROM person;")
	cur.execute(result_query)
	data = cur.fetchall()
	for row in data:
		print("Name: "+row[2] +" " +row[1] + "\nUID: " + row[3])
		
	cur.close()
	mariadb_connection.close()

if __name__ == "__main__":
	create()
	fetchResults()
