from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty


class StartScreen(ScreenManager):
    events_callback = ObjectProperty(lambda: None)
