from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Rectangle

from datetime import datetime

def clearAllFields(instance):
    for child in instance.parent.children:
        if child.__class__.__name__ == "TextInput":
            child.text = ""
    if instance.parent.__class__.__name__ == "SelectionFields":
        instance.parent.doorsBtn.text = "Any"

class LoginScreen(GridLayout):
    def __init__(self, intManager,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.intManager = intManager

        self.cols = 2

        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        btn1 = Button(text='Log  in', font_size=14)
        # btn1.bind(on_press=logInFunc)
        self.add_widget(btn1)

        clearBtn = Button(text='Clear all fields', font_size=14)
        clearBtn.bind(on_press=clearAllFields)
        self.add_widget(clearBtn)


class InterfaceManager(BoxLayout):
    def __init__(self, **kwargs):
        super(InterfaceManager, self).__init__(**kwargs)
        self.col = 1
        self.logInScreen = LoginScreen(self)
        self.add_widget(self.logInScreen)

class MyApp(App):

    def build(self):
        return InterfaceManager(orientation='vertical')

if __name__ == '__main__':
    MyApp().run()