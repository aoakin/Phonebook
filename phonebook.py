# phonebook
# Ayo Akinrinade 08.15.18

import os

def menu():
	print("Phonebook")
	print("=================")
	print("1. View Contacts")
	print("2. Add Contact")
	print("3. Remove Contact")
	print("4. Exit")
	print("=================")
	menu_choice = input(": ")
	if menu_choice == "1":
		view_contacts()
	elif menu_choice == "2":
		add_contact()
	elif menu_choice == "3":
		remove_contact()
	elif menu_choice == "4":
		exit()
	else:
		print("Please enter one of the given choices")
		menu()
def view_contacts():

	phonebook_db = 'phonebook.txt'
	f = open(phonebook_db, 'r')
	print("First Name | Last Name | Phone No.")
	print("==================================")
	contact_array = f.read()
	print(contact_array)
	f.close()
	print("- End of Contacts -\n")
	input("Press ENTER to continue\n\n")
	menu()

def add_contact():

	fname_in = input("First Name: ")
	lname_in = input("Last Name: ")
	phone_in = input("Phone No.: ")
	phonebook_db = 'phonebook.txt'
	f = open(phonebook_db, 'a+') # open file in append mode and creates the file if it doesn't exist
	f.write(fname_in + " " + lname_in + " " + phone_in + "\n")
	f.close()
	print("Entered Contact!\n")
	input("Press ENTER to continue\n\n")
	menu()
	
def remove_contact():
	print("- Incomplete -\n\n")

	# view all contacts

	phonebook_db = 'phonebook.txt'
	f = open(phonebook_db, 'r')
	print("First Name | Last Name | Phone No.")
	print("==================================")
	contact_array = f.read()
	print(contact_array)
	f.close()
	print("- End of Contacts -\n")

	# identify contact to delete by phone no.

	f = open(phonebook_db, 'r+')
	contact_to_del = input("Enter the Phone No. of contact you would like to delete:")
	for line in f:
		if contact_to_del in line:
			line = line.replace(contact_to_del, '')
		else:
			f.seek(0)
			f.truncate()
			f.write(line)
	f.close()
	print("\nDeleted Contact!\n")
	input("Press ENTER to continue\n\n")
	menu()

menu()
