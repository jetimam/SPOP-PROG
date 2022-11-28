from Game import Game
from os import listdir

class GameLibrary():
	def __init__(self, games=[]) -> None:
		self.games:list[Game] = games
	
	def __repr__(self) -> str:
		str = ''
		for game in self.games:
			str += game
			str += '\n'
		return str

	def add(self, name:str) -> None:
		if name+'.csv' in listdir('games/'):
			for game in self.games: #overriding previous game entry with the new game entry
				if game.name == name:
					self.games.pop(self.games.index(game))
					break
			self.games.append(Game(name))
			print(name + ' added!')
		else:
			print(name + ' couldn\'t be found.')

	def remove(self, name:str) -> None:
		for game in self.games:
			if game.name == name:
				self.games.pop(self.games.index(game))
				print(name + ' removed.')
				return None
		print(name + ' couldn\'t be found.')