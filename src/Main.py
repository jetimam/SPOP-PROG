'''
Date: 14/11/2022
Time: 16:34
Author: Umut Ucak
Product name: Video Game Dashboard Manager
Project General Description: This project\'s aim is creating a customizable CLI video game 
dashboard where the user can pick and choose what types of data about the video games that 
they are playing they wish to see.
File Contents: Main file where the program will be started.
'''

running = True
menu_print = '''
1. Add Game
2. View Library
3. Remove Game
4. Create Dashboard
5. Remove Dashboard
6. View List of Dashboards
7. Choose Dashboard
8. Filter Current Dashboard\'s Contents
9. View Dashboard
'''

print('Welcome to the video game dashboard manager!')
while(running):
	choice = input(menu_print)
	if choice == '1':
		pass
	elif choice == '2':
		pass
	elif choice == '3':
		pass
	elif choice == '4':
		pass
	elif choice == '5':
		pass
	elif choice == '6':
		pass
	elif choice == '7':
		pass
	elif choice == '8':
		pass
	elif choice == '9':
		pass
	elif choice == 'quit':
		print('buh-bye')
		break
	else:
		print('try again')
		continue