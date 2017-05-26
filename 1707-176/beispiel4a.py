from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

class Screen(BoxLayout):
    beschriftung = StringProperty(None)

class Beispiel4aApp(App):
    def build(self):
        s = self.root
        s.beschriftung = 'Beispiel4a'

if __name__ == "__main__":
    Beispiel4aApp().run()
