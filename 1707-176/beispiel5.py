from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

class Screen(BoxLayout):
    beschriftung = StringProperty(None)

class Beispiel5App(App):
    def build(self):
        s = self.root
        s.beschriftung = 'Beispiel5'

if __name__ == "__main__":
    Beispiel5App().run()
