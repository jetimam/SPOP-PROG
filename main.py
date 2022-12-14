'''
Date: 28/11/2022
Time: 12:30
Author: Umut Ucak
Product name: Video Game Dashboard Manager
Project General Description: This project\'s aim is creating a customizable CLI video game 
dashboard where the user can pick and choose what types of data about the video games that 
they are playing they wish to see.
File Contents: Main file where the program will be started.
'''

from DashboardLibrary import DashboardLibrary
from Dashboard import Dashboard
from GameLibrary import GameLibrary

running = True
dashboard_id = 1
dashboard_library = DashboardLibrary()
game_library = GameLibrary()

menu_print = '''1. Add Game
2. View Library
3. Remove Game
4. Create Dashboard
5. Remove Dashboard
6. View List of Dashboards
7. Choose Dashboard
8. Filter Current Dashboard\'s Contents
9. View Dashboard
10. Exit Program
'''

print('Welcome to the video game dashboard manager!')
while(running):
	choice = input(menu_print)
	if choice == '1':
		name = input('What is the name of the game you want to add? ')
		game_library.add(name)
	elif choice == '2':
		print(game_library)
	elif choice == '3':
		name = input('What is the name of the game you want to remove? ')
		game_library.remove(name) 
	elif choice == '4':
		id = int(input('What is the ID of the game you want to create a dashboard for? You can see the ID of a game by viewing the entire game library via using option 2 from the main menu. Enter 0 if you wish to go back and check: '))
		if id == 0:
			continue
		try:
			dashboard_library.add(Dashboard(game_library.games[id-1], dashboard_id))
			dashboard_id += 1
		except:
			print('Invalid ID')
	elif choice == '5':
		dashboard_library.remove()
	elif choice == '6':
		print(dashboard_library)
	elif choice == '7':
		dashboard_library.choose()
	elif choice == '8':
		dashboard_library.chosen.configure_filters()
	elif choice == '9':
		print(dashboard_library.chosen)
	elif choice == '10':
		print('buh-bye')
		running = False
	else:
		print('try again')
		continue