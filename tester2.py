from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from kivymd.app import MDApp

# Designate Our .kv design file 
Builder.load_file('tester2.kv')

class MyLayout(Widget):
	pass	

class AwesomeApp(MDApp):
	def build(self):
		return MyLayout()



if __name__ == '__main__':
	AwesomeApp().run()



