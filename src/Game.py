class Game():
	def __init__(self, name) -> None:
		self.name = name
		self.headers, self.data = self.load()

	def __repr__(self) -> str:
		print(self.name)

	def load(self) -> None:
		pass