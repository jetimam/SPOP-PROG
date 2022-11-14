from Game import Game
import random

class Dashboard():
	def __init__(self, game:Game, id:int, filters=[]) -> None:
		self.game = game
		self.filters = filters
		self.id = id

	def __repr__(self) -> str:
		pass

	def configure_filters(self) -> None:
		pass