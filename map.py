from kivymd.app import MDApp
from kivy_garden.mapview import MapView


class MapViewApp(MDApp):
	def build(self):
		mapview = MapView(zoom=10, lat=36, lon=-115)
		return mapview


MapViewApp().run()

