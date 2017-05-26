import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


# class GiveInScreen(AnchorLayout):
#
#
#     def btn_pressed(self, instance):
#         print ('pos: printed from root widget:')
#
#     def __init__(self, **kwargs):
#         super(GiveInScreen, self).__init__(**kwargs)
#         self.anchor_x = "right"
#         self.anchor_y = "bottom"
#         self.add_widget(Label(text = "Wie oft soll gewürfelt werden?"))
#         self.menge = TextInput(multiline = False)
#         self.add_widget(self.menge)
#         self.add_widget(Label(text = "(C) 2017 by Jonathan Weth, Lübeck"))
#         self.add_widget(Button(text='btn 1', on_press=self.btn_pressed))
#         self.add_widget(Button(text='btn 2'))



# class StartScreen(GridLayout):
#
#     def __init__(self, **kwargs):
#         super(StartScreen, self).__init__(**kwargs)
#         self.cols = 1
#         # self.add_widget(Label(text = "Wie oft soll gewürfelt werden?"))
#         # self.menge = TextInput(multiline = False)
#         # self.add_widget(self.menge)
#         # self.add_widget(Label(text='password'))
#         # self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)
class Wuerfel(Widget):
    pass


class WuerfelApp(App):

    def build(self):
        return Wuerfel()


if __name__ == "__main__":
    WuerfelApp().run()
