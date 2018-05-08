#!/user/bin/env python
#Menu.py
#created by James Vanaselja

import Read as read
import create
import copy
import sys

while True:
	select = int(raw_input("1.Read\n2.Create\n3.Copy\n4.Find\n5.Quit\nEnter a command..."))
	print("Select is : " + str(select))
	if (select == 1):
	#assigns a new card number to an existing user
		print("Reading...\n")
		read.main()
		break
	elif (select ==2):
	#Creates a new user in the database 
		print("Create New User\n")
		create.create()
		break
	elif (select == 3):
	#copies a card number from one user to another user
		print("Copy card ID\n")
		copy.copy()
		break
	elif (select == 4):
	#locates a user in the database
		print("find user\n")
		break;
	elif (select ==5):
		print("Program is now quitting...")
		sys.exit(1)
	else:
		print("Not a valid selection. Try again\n")
