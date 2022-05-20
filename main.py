# import requests
# import json
import os
import sys
import traceback

# import kivy
# from kivy.app import App

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.clock import Clock, _default_time
from kivy.properties import ObjectProperty, DictProperty

# from Libs.ux import customsettings
from Libs.ux.dialogs import dialog
from Libs.ux.startscreen import StartScreen

from Libs import programdata as data

MAX_TIME = 1/60.

# Приветственный экран - пустая начальная поделка
KV = """
MDScreen:

    FitImage:
        source: '/Users/olga/PycharmProjects/MiraApp/Data/Img/background.jpeg'

    MDRaisedButton:
        padding: 30
        text: "[b][color=#f3fbf5]Приветствуем вас в[/color] [color=#328b45]~Мира~[/color][/b]"
        halign: 'center'
        md_bg_color: 0, 0, 0, 0
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class NavDrawer(MDNavigationDrawer):
    events_callback = ObjectProperty()


class MobileApp(MDApp):
    # settings_cls = customsettings.CustomSettings
    # customsettings.TEXT_INPUT = data.string_lang_enter_value
    nav_drawer = ObjectProperty()
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def __init__(self, **kvargs):
        super(MobileApp, self).__init__(**kvargs)
        Window.bind(on_keyboard=self.events_program)

        self.window = Window
        self.dialog_load_contact = None
        self.open_exit_dialog = None
        self.scren_add_groups = None  # kivy.lang.builder.AddContactAddGroups
        # self.data = data
        self.current_tab = 'contacts'
        self.load_all_kv_files()

    def build(self):
        self.use_kivy_settings = False
        self.title = "Опросник Мира"
        self.icon = 'data/images/logo.png'

        # self.root = Builder.load_string(KV)
        # time.sleep(2)
        self.config = ConfigParser()
        self.config.read('{}/program.ini'.format(data.prog_path))

        self.screen = StartScreen(events_callback = self.events_program)
        self.manager_tab_classes = self.screen.ids.screen_manager_tab_classes
        self.manager_tab_sets = self.screen.ids.screen_manager_tab_sets
        self.manager_tab_reports = self.screen.ids.screen_manager_tab_reports
        self.manager_tab_scores = self.screen.ids.screen_manager_tab_scores

        self.nav_drawer = NavDrawer(title=data.string_lang_menu)
        self._check_existence_classes()
        self.info_classes, self.info_sets, self.info_reports, self.info_scores = self._read_data()
        self.old_info_sets = self.info_sets
        if self.info_classes.__len__():  # Activity со списком контактов
            Clock.schedule_interval(self.load_contacts, 0)

        return self.screen

    def load_contacts(self, interval):
        if not self.dialog_load_contact:
            self.dialog_load_contact = dialog(
                title=data.string_lang_wait[:-3],
                text=data.string_lang_classes_load, dismiss=False
            )

        while _default_time() < (Clock.get_time() + MAX_TIME):
            self.show_classes(self.info_classes)
            self.dialog_load_contact.dismiss()
            Clock.unschedule(self.load_contacts)

    def events_program(self, *args):
        # Вызывается при выборе одного из пунктов меню программы.

        if len(args) == 2:  # нажата ссылка
            event = args[1]
        else:  # нажата кнопка программы
            try:
                _args = args[0]
                event = _args if isinstance(_args, str) else _args.id
            except AttributeError:  # нажата кнопка девайса
                event = args[1]

        if data.PY2:
            if isinstance(event):
                event = event.encode('utf-8')

        if event == data.string_lang_settings:
            self.open_settings()
        elif event == data.string_lang_exit_key:
            self.exit_program()
        elif event == data.string_lang_license:
            self.show_license()
        elif event == data.string_lang_plugin:
            self.show_plugins()
        elif event in (1001, 27):
            self.back_screen(event)
        elif event == 'About':
            self.show_about()

        return True

    def back_screen(self, event):
        # Менеджер экранов.

        # Нажата BackKey на главном экране.
        if event in (1001, 27):
            if self.current_tab == 'contacts':
                if self.manager_tab_classes.current == 'create_contact':
                    if self.manager_tab_classes.has_screen('contact_list'):
                        self.manager_tab_classes.current = 'contact_list'
                        self._clear_form_create_class()
                    else:
                        self.manager_tab_classes.current = 'empty_contacts_list'
                else:
                    self.exit_program()
                    return

    def exit_program(self, *args):
        def close_dialog():
            self.open_exit_dialog.dismiss()
            self.open_exit_dialog = None

        if self.open_exit_dialog:
            return

        self.open_exit_dialog = dialog(
            text=data.string_lang_exit, title=self.title, dismiss=False,
            buttons=[
                [data.string_lang_yes, lambda *x: sys.exit(0)],
                [data.string_lang_no, lambda *x: close_dialog()]
            ]
        )

    def load_all_kv_files(self):
        directory_kv_files = '{}/Libs/ux'.format(self.directory)

        for kv_files in os.listdir(directory_kv_files):
            if kv_files == 'bugreporter.kv':
                continue
            Builder.load_file('{}/{}'.format(directory_kv_files, kv_files))

    def add_screens(self, name_screen, screen_manager, new_screen):
        screen = Screen(name=name_screen)  # cоздаем новый экран
        screen.add_widget(new_screen)  # добавляем Activity в созданный экран
        screen_manager.add_widget(screen)  # добавляем экран в менеджер экранов
        screen_manager.current = name_screen  # указываем менеджеру имя Activity, которое должно стать  текущим экраном приложения

    def on_tab_press(self, name_tab_press):
        # Вызывается при переключении TabbedPanel.

        self.current_tab = name_tab_press
        self.screen.ids.action_bar.title = self.data.title_bar[name_tab_press]

        if name_tab_press == 'groups':
            self._check_existence_classes()
            info_classes, self.info_sets, self.info_reports, self.info_scores = self._read_data()

            if not self.info_sets.__len__():
                if self.manager_tab_sets.current == 'empty_groups_list':
                    self.empty_screen_sets = \
                        self.manager_tab_sets.current_screen.children[0]

                    if not self.info_sets.__len__():
                        self.empty_screen_sets.ids.float_act_btn.disabled = \
                            True
                    else:
                        self.empty_screen_sets.ids.float_act_btn.disabled = \
                            False
            else:
                self._show_set(self.info_sets)
            if self.info_classes.__len__() and not self.info_sets.__len__():
                self.empty_screen_sets.ids.label.text = \
                    data.string_lang_not_sets
                self.empty_screen_sets.ids.float_act_btn.disabled = False

    def on_pause(self):
        # Ставит приложение на 'паузу' при выхоже из него. В противном случае запускает программу по заново'''
        return True

# if __name__ == "__main__":
#     MobileApp().run()

# ------------------------------- ЧАСТЬ MAIN ------------------------------------------

__version__ = '0.0.1'
sys.dont_write_bytecode = True
directory = os.path.split(os.path.abspath(sys.argv[0]))[0]


try:
    import webbrowser
    import six.moves.urllib

    import kivy
    kivy.require('1.9.1')

    from kivy.app import App
    from kivy.config import Config

    # Указываем пользоваться системным методом ввода, использующимся на
    # платформе, в которой запущенно приложение.
    Config.set('kivy', 'keyboard_mode', 'system')
    Config.set('graphics', 'width', '350')
    Config.set('graphics', 'height', '600')

    # Activity баг репорта.
    from Libs.ux.bugreporter import BugReporter
except Exception:
    traceback.print_exc(file=open('{}/error.log'.format(directory), 'w'))
    sys.exit(1)


def main():
    app = None

    try:
        from Libs.loadplugin import load_plugin  # загрузка плагинов

        # Запуск приложения.
        app = MobileApp()
        load_plugin(app)
        app.run()
    except Exception:
        text_error = traceback.format_exc()
        open('{}/error.log'.format(directory), 'w').write(text_error)
        print(text_error)

        if app:  # очищаем экран приложения от всех виджетов
            try:
                app.screen.clear_widgets()
            except AttributeError:
                pass

        class Error(MobileApp):
            # Выводит экран с текстом ошибки.

            def callback_report(self, *args):
                # Функция отправки баг-репорта'''

                try:
                    txt = six.moves.urllib.parse.quote(
                        self.win_report.txt_traceback.text.encode('utf-8'))
                    url = 'https://github.com/HeaTTheatR/DemoKivyContacts/issues/new?body=' + txt
                    webbrowser.open(url)
                except Exception:
                    sys.exit(1)

            def build(self):
                self.win_report = BugReporter(
                    callback_report=self.callback_report,
                    txt_report=text_error,
                    icon_background='data/images/logo.png'
                )

                return self.win_report

        Error().run()


if __name__ in ('__main__', '__android__'):
    main()
