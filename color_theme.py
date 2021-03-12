from kivy.lang import Builder
from kivymd.app import MDApp

#‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, 
#‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, 
#‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, 
#‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, 
#‘Brown’, ‘Gray’, ‘BlueGray’.
class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Indigo"
		self.theme_cls.accent_palette = "Red"
		return Builder.load_file('color_theme.kv')

		

MainApp().run()