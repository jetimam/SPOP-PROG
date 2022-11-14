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

from DashboardLibrary import DashboardLibrary
from Dashboard import Dashboard
from GameLibrary import GameLibrary

running = True
dashboard_id = 0
dashboard_library = DashboardLibrary()
game_library = GameLibrary()
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
		name = input('What is the name of the game you want to add?')
		game_library.add(name)
	elif choice == '2':
		print(game_library)
	elif choice == '3':
		name = input('What is the name of the game you want to remove?')
		game_library.remove(name)
	elif choice == '4':
		name = input('What is the name of the game you want to create a dashboard for?')
		i = game_library.games.index(name)
		dashboard_library.add(Dashboard(game_library[i], dashboard_id))
		dashboard_id += 1
	elif choice == '5':
		pass
	elif choice == '6':
		print(dashboard_library)
	elif choice == '7':
		dashboard_library.choose()
	elif choice == '8':
		dashboard_library.chosen.configure_filters()
	elif choice == '9':
		dashboard_library.view_chosen()
	elif choice == 'quit':
		print('buh-bye')
		break
	else:
		print('try again')
		continue