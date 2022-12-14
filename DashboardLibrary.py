from Dashboard import Dashboard

class DashboardLibrary():
	def __init__(self, dashboards=[], chosen=None) -> None:
		self.dashboards:list[Dashboard] = dashboards
		self.chosen:Dashboard = chosen

	def __repr__(self) -> str:
		out = ''
		for i in range(len(self.dashboards)):
			out += str(i+1) + ') ' + self.dashboards[i].game.name + '\n' + '  ID: ' + str(self.dashboards[i].id) + '\n' + '  Filters: ' + str(self.dashboards[i].filters) + '\n'
		return out
		# str = ''
		# c = 0
		# for dashboard in self.dashboards:
		# 	fields, _ = dashboard.import_data()
		# 	fields_str = ''
		# 	for i in range(fields):
		# 		if i in dashboard.filters:
		# 			fields_str += fields[i] + ' '
		# 	str += str(c+1) + ') ' + 'Game: ' + dashboard.game + '\n' + 'Filters Applied: ' + fields_str + '\n'
		# return str

	def choose(self) -> None:
		print('Please choose your main dashboard by entering the index of the dashboard you want.\n' + self)
		s = input()
		if not s.isnumeric():
			print('Invalid input. Enter only numbers.')
		else:
			s = int(s)-1
			if s > len(self.dashboards) or s < 1:
				print('Invalid input. Do not enter an index that is not mentioned above.')
			else:
				self.chosen = self.dashboards[s]
				print('New dashboard chosen!')

	def view_chosen(self) -> None:
		fields, _ = self.chosen.import_data()
		fields_str = ''
		for i in range(fields):
			if i in self.chosen.filters:
				fields_str += fields[i] + ' '
		print('Game: ' + self.chosen.game + '\n' + 'Filters Applied: ' + fields_str)

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