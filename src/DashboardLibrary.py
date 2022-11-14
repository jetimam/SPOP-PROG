from Dashboard import Dashboard

class DashboardLibrary():
	def __init__(self, dashboards:list[Dashboard]=[], chosen:Dashboard=None) -> None:
		self.dashboards = dashboards
		self.chosen = chosen

	def choose_dashboard(self) -> None:
		pass

	def view_chosen(self) -> None:
		print(self.chosen)

	def add_dashboard(self, dashboard:Dashboard) -> None:
		pass

	def remove_dashboard(self, index:int) -> None:
		pass

	def get_index(self, name:str) -> int:
		for i in range(len(self.dashboards)):
			if name == self.dashboards[i].game.name:
				return i