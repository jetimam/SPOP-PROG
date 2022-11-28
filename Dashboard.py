from Game import Game

class Dashboard():
	def __init__(self, game:Game, id:int, filters=[]) -> None:
		self.game = game
		self.filters = filters #the indices if the fields we do not want to see
		self.id = id

	def __repr__(self) -> str:
		for i in range(len(self.game.fields)):
			if i in self.filters:
				self.game.fields.pop(i)
				[self.game.data[j].pop(i) for j in range(len(self.game.data))]
		str = ''
		for i in range(len(self.game.fields)):
			str += str(self.game.fields[i]) + ': ' + str(self.game.data[i]) + '\n'
		return str

	def configure_filters(self) -> None:
		print('Choose the index of the filters you wish to remove. Enter them in a single line with spaces separating them.')
		[print(str(i+1) + ') ' + str(self.game.data[i])) for i in range(len(self.game.fields))]
		indices = input().split()
		[indices.pop(i) for i in range(len(indices)-1, 0, -1) if indices.count(indices[i]) > 1] #remove dupes
		success = True
		for i in range(len(indices)):
			if not indices[i].isnumeric():
				print('Invalid input. Enter only numbers.')
				success = False
				break
			else:
				indices[i] = int(indices[i])-1
				if indices[i] > len(self.game.fields) or indices[i] < 1:
					print('Invalid input. Do not enter an index that is not mentioned above.')
					success = False
					break
		if success:
			self.filters.clear()
			[self.filters.append(i) for i in indices]
			print('Filters updated!')