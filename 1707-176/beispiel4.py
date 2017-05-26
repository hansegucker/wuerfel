from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

class Screen(BoxLayout):
    beschriftung = StringProperty(None)

class Beispiel4App(App):
    def build(self):
        s = self.root
        s.beschriftung = 'Beispiel4'

if __name__ == "__main__":
    Beispiel4App().run()
