
#!/user/bin/env python
#Created by James Vanaselja
import RPi.GPIO as GPIO
import SimpleMFRC522
import sys
import signal
import mysql.connector as mariadb
import re
import secrets

def main():
	mariadb_connection = mariadb.connect(user=secrets.user, password=secrets.password, database=secrets.database)
#testing comments
	cursor = mariadb_connection.cursor(buffered=True)
	cursor2 = mariadb_connection.cursor(buffered=True)
#cursor.execute("SELECT * FROM person where LastName = 'smith';")
#print(cursor.fetchall())
	print("Please scan a card to begin...")
	data = []
	continue_read = True
	def signal_handler(signal, frame):
		print('End Read')
		continue_read = False
		GPIO.cleanup
		sys.exit(0)

	signal.signal(signal.SIGINT, signal_handler)

#instantiate reader object
	reader = SimpleMFRC522.SimpleMFRC522()
#while continue_read:
	
	try:
		id, text = reader.read()
		UID = str(id)
		re.sub("[^0-9]","",UID)
	#	print('UID: ' + str(id))
	#	print('Data: ' + text)
		data = [id,str(text)]
		chosen_user = raw_input("Pick a user by last name to assign a card number:")

		print(chosen_user)		
		stmt1 =("SELECT * FROM person;")
		stmt2 =("UPDATE person SET UID=%s WHERE LastName=%s;")   	
		cursor.execute(stmt1)
		cursor2.execute(stmt2,[UID,chosen_user])

		mariadb_connection.commit()
		if(cursor2.rowcount>0):
			print("Read Successful")
		for (personID, LastName, FirstName, UID) in cursor:
			print("Name: {},{}\n UID: {}" .format(LastName,FirstName, UID))
	except:
		print("an error has occured")
	finally:
		GPIO.cleanup()
		output = ''
	for x in text:
		output = output + str(ord(x)) +' '
	print('Data as ASCII: ' + output) 
	mariadb_connection.close()

if __name__ == '__main__':
	main()
	

