import os
import sys


from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty


class BugReporter(FloatLayout):
    title = 'Bug reporter'
    label_info_for_user = StringProperty('Sorry, an error occurred in the '
                                         'program!')
    info_for_user = StringProperty('You can report this bug using'
                                   'the button bellow, helping us to fix it.')
    txt_report = StringProperty('')

    callback_clipboard = ObjectProperty(lambda: None)
    # Функция копирования баг-репорта в буфер обмена"""

    callback_report = ObjectProperty(lambda: None)
    # Функция отправки баг-репорта"""

    report_readonly = BooleanProperty(False)
    # Запрещено ли редактировать текст ошибки"""

    icon_background = StringProperty('Data/Img/logo.png')
    # Фоновое изображение окна"""

    txt_button_clipboard = StringProperty('Copy Bug')
    txt_button_report = StringProperty('Report Bug')
    txt_button_close = StringProperty('Close')
    # Подписи кнопок"""

    Builder.load_file('{}/Libs/ux/kv/bugreporter.kv'.format(
        os.path.split(os.path.abspath(sys.argv[0]))[0].split("/Libs/ux")[0]))
    # Макет интерфейса"""

    def __init__(self, **kwargs):
        super(BugReporter, self).__init__(**kwargs)

        if not os.path.exists(self.icon_background):
            self.icon_background = 'Data/Img/logo.png'

        name_funcs_buttons = {
            self.txt_button_clipboard: self.callback_clipboard,
            self.txt_button_report: self.callback_report}

        for name_button in name_funcs_buttons.keys():
            if callable(name_funcs_buttons[name_button]):
                self.ids.box_layout.add_widget(
                    Button(text=name_button,
                           on_press=name_funcs_buttons[name_button]))

    def on_close(self, *args):
        from kivy.app import App
        App.get_running_app().stop()
