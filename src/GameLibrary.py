from Game import Game

class GameLibrary():
	def __init__(self, games:list[Game]=[]) -> None:
		self.games = games
	
	def __repr__(self) -> str:
		str = ''
		for game in self.games:
			str += game
			str += '\n'
		return str

	def add_game(self, name:str) -> None:
		pass

	def remove_game(self, index:int) -> None:
		pass