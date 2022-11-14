class Game():
	def __init__(self) -> None:
		self.headers = []
		self.data = []

	def __repr__(self) -> str:
		print(self.headers)
		print(self.data)