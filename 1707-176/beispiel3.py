from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Screen(BoxLayout):
    beschriftung = StringProperty(None)

class Beispiel3App(App):
    def build(self):
        s = self.root
        s.beschriftung = 'Beispiel3'

if __name__ == "__main__":
    Beispiel3App().run()
