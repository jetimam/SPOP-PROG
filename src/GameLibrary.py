from Game import Game

class GameLibrary():
	def __init__(self, path:str, games:list[Game]=[]) -> None:
		self.games = games
		self.path = path # the absolute path to the dir with the game data.
	
	def __repr__(self) -> str:
		str = ''
		for game in self.games:
			str += game
			str += '\n'
		return str

	def add_game(self) -> None:
		pass

	def remove_game(self, name:str) -> None:
		pass