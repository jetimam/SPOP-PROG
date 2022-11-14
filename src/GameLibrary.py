from Game import Game

class GameLibrary():
	def __init__(self, games=[]) -> None:
		self.games = games
	
	def __repr__(self) -> str:
		str = ''
		for game in self.games:
			str += game
			str += '\n'
		return str

	def add(self, name:str) -> None:
		pass

	def remove(self, index:int) -> None:
		pass