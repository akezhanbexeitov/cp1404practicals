from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

CONSTANT = 0.62137


class Converter(App):
    message = StringProperty()

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_press(self, miles):
        if miles <= 0:
            self.message = "0.0"
        else:
            km = miles / CONSTANT
            self.message = "{:.3f}".format(km)

    def handle_convert(self, miles):
        if miles <= 0:
            self.root.ids.output.text = "0.0"
        else:
            km = miles / CONSTANT
            self.root.ids.output.text = "{:.3f}".format(km)

    def handle_up(self):
        self.root.ids.user_input.text = "1"
        self.root.ids.output.text = "1.609"

    def handle_down(self):
        self.root.ids.user_input.text = "-1"
        self.root.ids.output.text = "0.0"


Converter().run()