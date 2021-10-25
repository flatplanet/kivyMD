from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.recycleview import RecycleView
from kivy.graphics import Color

Builder.load_string('''
<RV>:
	viewclass: 'Label'
	background_color: 1,0,0,.5
	RecycleBoxLayout:
		size_hint_y: None
		height: self.minimum_height
		default_size: None, 100
		default_size_hint: 1, None
		orientation: 'vertical'
		background_color: 1,0,0,.5
		

''')

class RV(RecycleView):
	def __init__(self):
		super().__init__()
		self.data = [{'text':str(i)} for i in range(100)]

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		
		#return Builder.load_file('rview2.kv')
		return RV()
	
	
MainApp().run()