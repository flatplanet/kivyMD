from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
	#texter = StringProperty()
	texter = "Variable!!"
	lister = [1,2,3,4,5]
	def build(self):

		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('code2.kv')

	
	
MainApp().run()