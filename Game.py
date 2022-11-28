import csv

class Game():
	def __init__(self, name:str) -> None:
		self.name = name
		self.fields, self.data = self.import_data()

	def __repr__(self) -> str:
		return self.name

	def import_data(self) -> tuple(list[str], list[str]):
		with open('games/' + self.name, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			data = next(csvreader)
			return (fields, data)