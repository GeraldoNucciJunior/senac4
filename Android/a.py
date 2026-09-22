from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        return Button(text="Olá, Android!")

MeuApp().run()