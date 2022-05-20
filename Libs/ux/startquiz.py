from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ObjectProperty, ListProperty


class StartQuiz(FloatLayout):
    callback = ObjectProperty(lambda: None)
    # avatar = StringProperty(None)
    name_class = StringProperty(None)
    number_set = StringProperty(None)
    # size_avatar = ListProperty((150, 150))