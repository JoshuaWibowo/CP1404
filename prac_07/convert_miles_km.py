"""
CP1404 Practical
Kivy GUI program to convert miles to km
Joshua Wibowo
Started 5/10/2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKmApp(App):
    """App that convert miles to km"""
    def build(self):
        """Build app"""
        Window.size = (720, 480)
        self.title = "Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
