from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
# Display Pixles

class MainApp(MDApp):
	def build(self):
		# Define Screen
		screen = Screen()
		# Define Table
		table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.5},
			size_hint =(0.9, 0.6),
			check = True,
			column_data = [
				("First Name", dp(30)),
				("Last Name", dp(30)),
				("Email Address", dp(30)),
				("Phone Number", dp(30))
			],
			row_data = [
				("John", "Elder", "john@codemy.com", "(123) 456-7891"),
				("Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),

			]


			)
		
		# Bind the table
		table.bind(on_check_press=self.checked)
		table.bind(on_row_press=self.row_checked)

		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		#return Builder.load_file('table.kv')
		# Add table widget to screen
		screen.add_widget(table)
		return screen
	
	# Function for check presses
	def checked(self, instance_table, current_row):
		print(instance_table, current_row)
	# Function for row presses
	def row_checked(self, instance_table, instance_row):
		print(instance_table, instance_row)


MainApp().run()