"""
CP1404 Practical
Kivy GUI program to convert miles to km
Joshua Wibowo
Started 5/10/2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    """App that convert miles to km"""

    def build(self):
        """Build app"""
        Window.size = (720, 480)
        self.title = "Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        """Handle calculation when pressed"""
        result = self.get_valid_value()
        result = result * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle the increase/decrease in the value"""
        value = self.get_valid_value()
        value += change
        self.root.ids.input_number.text = str(int(value))
        self.handle_convert(value)

    def get_valid_value(self):
        """Check if value is valid"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKmApp().run()
