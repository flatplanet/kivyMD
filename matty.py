from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

# Define what we want to graph
x = [1,2,3,4,5]
y = [5, 12, 6, 9, 15]

plt.plot(x,y)
plt.ylabel("This is MY Y Axis")
plt.xlabel("X Axis")


class Matty(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		box = self.ids.box
		box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

	def save_it(self):
		name = self.ids.namer.text
		if name:
			plt.savefig(name)



class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		Builder.load_file('matty.kv')
		return Matty()



MainApp().run()
