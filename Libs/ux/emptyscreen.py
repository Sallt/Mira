from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty


class EmptyScreen(FloatLayout):
    image = StringProperty()
    text = StringProperty()
    callback = ObjectProperty()
    disabled = BooleanProperty()
