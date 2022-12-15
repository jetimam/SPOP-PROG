from Game import Game

class Dashboard():
	def __init__(self, game:Game, id:int) -> None:
		self.game = game
		self.filters = range(len(game.fields)) #the indices if the fields we do not want to see
		self.id = id

	def __repr__(self) -> str:
		return 'Game: ' + self.game.name + '\n' + 'Dashboard ID: ' + str(self.id)
		
		# for i in range(len(self.game.fields)):
		# 	if i in self.filters:
		# 		self.game.fields.pop(i)
		# 		[self.game.data[j].pop(i) for j in range(len(self.game.data))]
		# str = ''
		# for i in range(len(self.game.fields)):
		# 	str += str(self.game.fields[i]) + ': ' + str(self.game.data[i]) + '\n'
		# return str

	def configure_filters(self) -> None:
		print('Choose the index of the filters you wish to remove. Enter them in a single line with spaces separating them.')
		[print(str(i+1) + ') ' + str(self.game.data[i])) for i in range(len(self.game.fields))]
		indices = input().split()
		[indices.pop(i) for i in range(len(indices)-1, 0, -1) if indices.count(indices[i]) > 1] #remove dupes
		for i in range(len(indices)):
			if not indices[i].isnumeric():
				print('Invalid input. Enter only numbers.')
				return None
			else:
				indices[i] = int(indices[i])-1
				if indices[i] >= len(self.game.fields) or indices[i] < 0:
					print('Invalid input. Do not enter an index that is not mentioned above.')
					return None
		indices.sort()
		self.filters = indices
		print('Filters updated!')