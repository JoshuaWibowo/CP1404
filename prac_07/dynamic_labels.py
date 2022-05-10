"""
CP1404 Practical
Kivy GUI program to demonstrate dynamic
Joshua Wibowo
Started 5/10/2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic labels creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_dict = {"Joshua", "Timothy", "James", "Michael"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        """Create labels from dictionary"""
        for name in self.name_dict:
            name_label = Label(text=name)
            self.root.ids.main.add_label(name_label)


DynamicLabelsApp().run()
