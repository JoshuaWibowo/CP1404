"""
CP1404 Practical
Kivy GUI program to demonstrate dynamic
Joshua Wibowo
Started 5/10/2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic labels creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_dict = {"Joshua", "Timothy", "James", "Michael"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from dictionary"""
        for name in self.name_dict:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)


DynamicLabelsApp().run()
