# importing the library to be used
import os
from datetime import datetime
from random import sample

login = False
staff_cred = {}

def main():
	choice = get_menu()

	while choice != 2:
		staff, time = staff_auth()
		create_session(staff, time)
		option = staff_options()

		while option != 3:

			if option == 1:
				action, time = create_cust()
				write_to_sess(staff, action, time)
			elif option == 2:
				action, time = get_acc_details()
				write_to_sess(staff, action, time)
			option = staff_options()
		remove_sess()
		choice = get_menu()
	
def get_menu():
	print('Welcome')
	print('1. Staff Login')
	print('2. Close App')
	print()

	choice = input('Enter an option: ')
	print()

	while choice not in ['1', '2']:
		choice = input('Enter the right option (1 or 2): ')

	return int(choice)


def create_session(staff, time):
	with open('session.txt', 'w') as sess:
		note = staff +' logged in at '+ str(time)+'\n'
		sess.write(note)

def write_to_sess(staff, action, time):
	with open('session.txt', 'a') as sess:
		note = staff+' '+action+' '+time+'\n'
		sess.write(note)

def staff_auth():
	
	global staff_cred
	with open('staff.txt', 'r') as staf:
		username = staf.readline().rstrip('\n')

		while username != '':
			staf_list = []
			password = staf.readline().rstrip('\n')
			staf_list.append(password)
			email = staf.readline().rstrip('\n')
			staf_list.append(email)
			fullname = staf.readline().rstrip('\n')
			staf_list.append(fullname)
			staff_cred[username] = staf_list

			username = staf.readline().rstrip()
	temp_username_login = ''
			
	print('Enter your login details:')
	username_login = input('Enter your username: ')
	password_login = input('Enter your password: ')
	temp_username_login = username_login
	print()

	while username_login not in staff_cred.keys() :
		print('Wrong username or password, try again')
		username_login = input('Enter your username: ')
		password_login = input('Enter your password: ')
		temp_username_login = username_login
		print()

	while (staff_cred[temp_username_login][0] != password_login):
		print('Wrong username or password, try again')
		username_login = input('Enter your username: ')
		password_login = input('Enter your password: ')
		print()

	return staff_cred[temp_username_login][-1] , datetime.now().strftime("%H:%M:%S")
	


def staff_options():
	print('1. Create new bank account')
	print('2. Check Account Details')
	print('3. Logout')
	print()

	option = input('Enter an option: ')
	print()

	while option not in ['1', '2', '3']:
		option = input('Enter the right option(1, 2 , 3): ')
		print()

	return int(option)

def create_cust():
	details = get_all_cust()
	print('Enter the customer details')
	acc_name = input('Account Name: ')
	while acc_name in details.keys():
		acc_name = input('Enter a different Account Name: ')

	open_bal = input('Opening Balance: ')
	acc_type = input('Account Type: ')
	acc_email = input('Account email: ')
	pop = '0123456789'
	passlen = 10

	# this will return a list of string
	acc_number = "".join(sample(pop , passlen))
	print('Your account number is ' + acc_number)


	with open('customer.txt', 'a') as cust:
		cust.write(acc_name+ '\n')
		cust.write(open_bal+ '\n')
		cust.write(acc_type + '\n')
		cust.write(acc_email+ '\n')
		cust.write(acc_number+ '\n')

	return 'Created an account with the name '+acc_name, datetime.now().strftime("%H:%M:%S")

def get_acc_details():

	details = get_all_cust()
	name = input('Enter the Account name of the customer: ')

	while name not in details.keys():
		print('The customer with the name '+name+' does not exit in the database')
		name = input('Enter account name of a customer: ')

	print('Account Name: '+name)
	print('Opening Balance: '+str(details[name][0]))
	print('Account Type: '+details[name][1])
	print('Account Email: '+details[name][2])
	print('Account Number: '+details[name][3])

	return 'checked the account detail of '+name, datetime.now().strftime("%H:%M:%S")

def get_all_cust():
	details = {}

	with open('customer.txt', 'r') as cust:
		acct_name = cust.readline().rstrip('\n')

		while acct_name != '':
			cust_list = []
			open_bal = cust.readline().rstrip('\n')
			cust_list.append(open_bal)

			acc_type = cust.readline().rstrip('\n')
			cust_list.append(acc_type)

			acc_email = cust.readline().rstrip('\n')
			cust_list.append(acc_email)

			acc_number = cust.readline().rstrip('\n')
			cust_list.append(acc_number)

			details[acct_name] = cust_list

			acct_name = cust.readline().rstrip('\n')

	return details

def remove_sess():
	os.remove('session.txt')

main()