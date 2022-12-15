from Dashboard import Dashboard

class DashboardLibrary():
	def __init__(self, dashboards=[], chosen=None) -> None:
		self.dashboards:list[Dashboard] = dashboards
		self.chosen:Dashboard = chosen

	def __repr__(self) -> str:
		out = ''
		c = 1
		for dashboard in self.dashboards:
			out += str(c) + ') ' + str(dashboard) + '\n\n'
			# out += str(i+1) + ') ' + self.dashboards[i].game.name + '\n' + '  ID: ' + str(self.dashboards[i].id) + '\n' + '  Filters: ' + str(self.dashboards[i].filters) + '\n'
		return out

	def choose(self) -> None:
		print('Please choose your main dashboard by entering the index of the dashboard you want.\n' + str(self))
		s = input()
		if not s.isnumeric():
			print('Invalid input. Enter only numbers.')
		else:
			s = int(s)-1
			if s >= len(self.dashboards) or s < 0:
				print('Invalid input. Do not enter an index that is not mentioned above.')
			else:
				self.chosen = self.dashboards[s]
				print('New dashboard chosen!')

	def view_chosen(self) -> None:
		fields = self.chosen.game.fields
		data = self.chosen.game.data
		filter_indices = []
		print('Game: ' + str(self.chosen.game) + '\n' + 'Latest Filtered Data:')
		[filter_indices.append(i) for i in range(len(fields)) if i in self.chosen.filters]
		filter_indices.sort()
		[print(' # ' + fields[i] + ': ' + data[i]) for i in filter_indices]

	def add(self, dashboard:Dashboard) -> None:
		self.dashboards.append(dashboard)
		print(' > Dashboard created for ' + str(dashboard.game.name))

	def remove(self) -> None:
		print('Please choose which dashboard you wish to remove.\n' + str(self))
		s = input()
		if not s.isnumeric():
			print('Invalid input. Enter only numbers.')
			return None
		s = int(s)-1
		if s >= len(self.dashboards) or s < 0:
			print('Invalid input. Do not enter an index that is not mentioned above.')
			return None
		self.dashboards.pop(s)
		print('Dashboard removed.')

	def get_index(self, name:str) -> int:
		for i in range(len(self.dashboards)):
			if name == self.dashboards[i].game.name:
				return i