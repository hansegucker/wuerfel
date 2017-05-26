from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

class ScreenManagement(ScreenManager):
    pass

class Main(Screen):
    beschriftung = StringProperty(None)

class Setup(Screen):
    pass

class Beispiel6App(App):
    def build(self):
        global SM
        SM = self.root
        s = SM.get_screen('main')
        s.beschriftung = 'Beispiel6'

if __name__ == "__main__":
    Beispiel6App().run()
