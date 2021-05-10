from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

	data = {
		"language-python": "Python",
		"language-ruby": "Ruby",
		"language-javascript": "JS"
	}
	
	def callback(self, instance):
		if instance.icon == 'language-python':
			lang = "Python"
		elif instance.icon == 'language-javascript':
			lang = "JS"
		elif instance.icon == 'language-ruby':
			lang = "Ruby"

		self.root.ids.my_label.text = f'You Pressed {lang}'

	#Open
	def open(self):
		self.root.ids.my_label.text = f'Open!!'		

	# Close
	def close(self):
		self.root.ids.my_label.text = f'Close!!!'				

	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('sd.kv')
	
	
MainApp().run()