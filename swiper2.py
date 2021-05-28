from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('swiper2.kv')
	# Swipe Left
	def on_swipe_left(self):
		self.root.ids.toolbar.title = "You Swiped Left!"
		#print("You Swiped Left!")

	# Swipe Right
	def on_swipe_right(self):
		self.root.ids.toolbar.title = "You Swiped Right!"
		#print("You Swiped Right!")	

MainApp().run()