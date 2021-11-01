from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('toe.kv')
	
	# Define Who's turn it is
	turn = "X"

	def presser(self, btn):
		if self.turn == 'X':
			btn.text = "X"
			btn.disabled = True
			self.root.ids.score.text = "O's Turn!"
			self.turn = "O"
		else:
			btn.text = "O"
			btn.disabled = True
			self.root.ids.score.text = "X's Turn!"
			self.turn = "X"


	def restart(self):
		# Reset Who's Turn It Is
		self.turn = "X"

		# Enable The Buttons
		self.root.ids.btn1.disabled = False
		self.root.ids.btn2.disabled = False
		self.root.ids.btn3.disabled = False
		self.root.ids.btn4.disabled = False
		self.root.ids.btn5.disabled = False
		self.root.ids.btn6.disabled = False
		self.root.ids.btn7.disabled = False
		self.root.ids.btn8.disabled = False
		self.root.ids.btn9.disabled = False

		# Clear The Buttons
		self.root.ids.btn1.text = ""
		self.root.ids.btn2.text = ""
		self.root.ids.btn3.text = ""
		self.root.ids.btn4.text = ""
		self.root.ids.btn5.text = ""
		self.root.ids.btn6.text = ""
		self.root.ids.btn7.text = ""
		self.root.ids.btn8.text = ""
		self.root.ids.btn9.text = ""

		# Reset The Score Label
		self.root.ids.score.text = "X GOES FIRST!"


	
MainApp().run()