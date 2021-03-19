from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('login.kv')
	def logger(self):
		self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'

	def clear(self):
		self.root.ids.welcome_label.text = "WELCOME"		
		self.root.ids.user.text = ""		
		self.root.ids.password.text = ""		
	
MainApp().run()