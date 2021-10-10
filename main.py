import kivy
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text="Hello World")
        return label


MainApp().run()
