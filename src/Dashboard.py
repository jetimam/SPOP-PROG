from Game import Game

class Dashboard():
	def __init__(self, game:Game, filters=[]) -> None:
		self.game = game
		self.filters = filters

	def __repr__(self) -> str:
		pass

	def configure_filters(self) -> None:
		pass