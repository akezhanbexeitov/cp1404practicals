from kivy.app import App
from kivy.app import Widget


class MyFirstKivy(App):

    def build(self):
        self.root = Widget()
        self.title = "My First Kivy"
        return self.root


if __name__ == '__main__':
    MyFirstKivy().run()