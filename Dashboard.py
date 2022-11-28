from Game import Game
import csv

class Dashboard():
	def __init__(self, game:Game, id:int, filters=[]) -> None:
		self.game = game
		self.filters = filters #the indices if the fields we do not want to see
		self.id = id

	def import_data(self) -> tuple(list[str], list[str]):
		with open('games/' + self.game, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			data = next(csvreader)
			return (fields, data)

	def __repr__(self) -> str:
		fields, data = self.import_data()
		for i in range(len(fields)):
			if i in self.filters:
				fields.pop(i)
				[data[j].pop(i) for j in range(len(data))]
		str = ''
		for i in range(len(fields)):
			str += str(fields[i]) + ': ' + str(data[i]) + '\n'
		return str

	def configure_filters(self) -> None:
		print('Choose the index of the filters you wish to remove. Enter them in a single line with spaces separating them.')
		fields, data = self.import_data()
		[print(str(i+1) + ': ' + str(data[i])) for i in range(len(fields))]
		indices = input().split()
		[indices.pop(i) for i in range(len(indices)-1, 0, -1) if indices.count(indices[i]) > 1] #remove dupes
		fail = False
		for i in range(len(indices)):
			if not indices[i].isnumeric():
				print('Invalid input. Do not enter letters, only numbers.')
				fail = True
			elif indices[i] > len(fields) or indices[i] < 1:
				print('Invalid input. Do not enter an index that is not mentioned above.')
				fail = True
			else:
				indices[i] = int(indices[i])
		if not fail:
			self.filters = indices
			print('Filters updated!')