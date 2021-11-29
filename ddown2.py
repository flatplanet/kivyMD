from kivy.lang import Builder
from kivymd.app import MDApp
#from kivymd.uix.screen import Screen


class MainApp(MDApp):
	title = "Simple List"
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
        
		return Builder.load_file('ddown2.kv')
	
	def presser(self, pressed, list_id):
		#self.root.ids.
		pressed.secondary_text = f"You pressed {list_id}"

MainApp().run()

