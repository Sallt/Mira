import os
from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import RiseInTransition
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.core.window import Window
from kivy.clock import Clock
# from kivymd.uix.screen import MDScreen
# from akivymd import *
# from kivy.uix.widget import Widget
# from libs import programdata as data
# from libs.uix.startscreen import StartScreen
# from libs.uix.dialogue import dialog
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout


class MobileApp(MDApp):

    def __init__(self, **kvargs):
        super(MobileApp, self).__init__(**kvargs)
        Window.bind(on_keyboard=self.events_program)
        # Clock.schedule_once(self._finish_init)

        # self.screen = StartScreen(events_callback=self.events_program)
        self.window = Window
        # self.dialog_load_contact = None
        # self.open_exit_dialog = None
        # self.screen_add_groups = None  # kivy.lang.builder.AddContactAddGroups
        # self.data = data
        self.current_tab = 'classes'

    def build(self):
        self.title = "Опросник Мира"
        self.icon = 'data/images/logo.png'
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.material_style = "M2"
        self.window.size = (400, 1200)
        # return self.load_kv_files()
        # Builder.load_file('libs/uix/kv/startscreen.kv')
        # self.screen = StartScreen()
        # self.manager_tab_classes = self.screen.ids.sm_tab_classes

        kv = Builder.load_file('libs/uix/kv/startscreen.kv')
        # return Builder.load_file('/Users/olga/PycharmProjects/Mira/libs/uix/kv/startscreen.kv')
        return kv
        # return self.screen
        # self.screen = self.screen
        # self.screen = StartScreen(events_callback=self.events_program)
        # self.manager_tab_classes = self.screen.ids.screen_manager_tab_classes
        # self.manager_tab_sets = self.screen.ids.screen_manager_tab_sets
        # self.manager_tab_reports = self.screen.ids.screen_manager_tab_reports
        # self.manager_tab_scores = self.screen.ids.screen_manager_tab_scores
        #
        # self.nav_drawer = NavDrawer(title=data.string_lang_menu)
        # self._check_existence_classes()
        # self.info_classes, self.info_sets, self.info_reports, self.info_scores = self._read_data()
        # self.old_info_sets = self.info_sets
        # if self.info_classes.__len__():  # Activity со списком контактов
        #     Clock.schedule_interval(self.load_contacts, 0)
        #
        # return self.screen

    def save_info_class(self):
        return

    def change_screen(self, scr_name):
        self.root.current = scr_name

    def show_form_create_class(self):
        # sm = ScreenManager(transition = RiseInTransition())
        # sm.add_widget(EmptyScreen(name='empty'))
        # sm.add_widget(CreateClass(name='cr_class'))
        # sm.switch_to(EmptyScreen)
        # return sm

        # self.manager_tab_classes.current = 'create_class'
        # self._form_create_contact = self.manager_tab_classes.current_screen.children[0]
        return CreateClass()

    def show_form_create_set(self):
        return

    def choose_class(self):
        print("you've tried to choose between unexistent classes !")
        return

    # def  load_kv_files(self):
    #     dir_kv_files = 'libs/uix/kv'

        # for kv_file in os.listdir(dir_kv_files):
        #     # if kv_files == 'bugreporter.kv':
        #     #     continue
        #     Builder.load_file('{}/{}'.format(dir_kv_files, kv_file))

    def choice_avatar_class(self):
        return

    def add_screens(self, name_screen, screen_manager, new_screen):
        # screen = Screen(name=name_screen)  # cоздаем новый экран
        # screen.add_widget(new_screen)  # добавляем Activity в созданный экран
        # screen_manager.add_widget(screen)  # добавляем экран в менеджер экранов
        # screen_manager.current = name_screen  # указываем менеджеру имя Activity, которое должно стать  текущим экраном приложения
        return

    def on_tab_press(self, name_tab_press):
         # Вызывается при переключении BottomNavigation.

        # self.current_tab = name_tab_press
        return
    #     self.screen.ids.home_bar.title = self.data.title_bar[name_tab_press]
    #
    #     if name_tab_press == 'sets':
    #         self._check_existence_classes()
    #         info_classes, self.info_sets, self.info_reports, self.info_scores = self._read_data()
    #
    #         if not self.info_sets.__len__():
    #             if self.manager_tab_sets.current == 'empty_sets_list':
    #                 self.empty_screen_sets = \
    #                     self.manager_tab_sets.current_screen.children[0]
    #
    #                 if not self.info_sets.__len__():
    #                     self.empty_screen_sets.ids.float_act_btn.disabled = \
    #                         True
    #                 else:
    #                     self.empty_screen_sets.ids.float_act_btn.disabled = \
    #                         False
    #         else:
    #             self._show_set(self.info_sets)
    #         if self.info_classes.__len__() and not self.info_sets.__len__():
    #             self.empty_screen_sets.ids.label.text = \
    #                 data.string_lang_not_sets
    #             self.empty_screen_sets.ids.float_act_btn.disabled = False

    def events_program(self, *args):
        # if len(args) == 2:  # нажата ссылка
        #     event = args[1]
        # else:  # нажата кнопка программы
        #     try:
        #         _args = args[0]
        #         event = _args if isinstance(_args, str) else _args.id
        #     except AttributeError:  # нажата кнопка девайса
        #         event = args[1]
        #
        # if event == data.string_lang_exit_key:
        #     self.exit_program()
        # elif event in (1001, 27):
        #     self.back_screen(event)
        # elif event == 'About':
        #     self.show_about()
        # elif event == 'Home':
        #     self.a()

        return True

    def on_pause(self):
        # Ставит приложение на 'паузу' при выходе из него. В противном случае запускает программу заново
        return True

    # def back_screen(self, event):
    #     # Менеджер экранов.
    #
    #     # Нажата BackKey на главном экране.
    #     if event in (1001, 27):
    #         if self.current_tab == 'classes':
    #             if self.manager_tab_classes.current == 'create_class':
    #                 if self.manager_tab_classes.has_screen('class_list'):
    #                     self.manager_tab_classes.current = 'class_list'
    #                     self._clear_form_create_class()
    #                 else:
    #                     self.manager_tab_classes.current = 'empty_classes_list'
    #             else:
    #                 self.exit_program()
    #                 return

    def exit_program(self, *args):
        # def close_dialog():
        #     self.open_exit_dialog.dismiss()
        #     self.open_exit_dialog = None
        #
        # if self.open_exit_dialog:
        #     return
        #
        # self.open_exit_dialog = dialog(
        #     text=data.string_lang_exit, title=self.title, dismiss=False,
        #     buttons=[
        #         [data.string_lang_yes, lambda *x: sys.exit(0)],
        #         [data.string_lang_no, lambda *x: close_dialog()]
        #     ]
        # )
        return


class StartScreen(Screen):
    pass


class ScoresheetScreen(Screen):
    pass


class QuizScreen(Screen):
    pass


class EmptyScreen(FloatLayout):
    image = StringProperty()
    text = StringProperty()
    callback = ObjectProperty()
    disabled = BooleanProperty()


class CreateClass(BoxLayout):
    checks = []

    def checkbox_click(self, instance, value, topping):
        if value == True:
            CreateClass.checks.append(topping)
            tops = ''
            for x in CreateClass.checks:
                tops = f'{tops} {x}'
            # self.ids.output_label2.text = f'You Selected: {tops}'
        else:
            CreateClass.checks.remove(topping)
            tops = ''
            for x in CreateClass.checks:
                tops = f'{tops} {x}'
            # self.ids.output_label2.text = f'You Selected: {tops}'


class CreateSet(BoxLayout):
    pass


class DisplayScores(BoxLayout):
    pass


class WindowManager(ScreenManager):
    pass


class NavDrawer(MDNavigationDrawer):
    events_callback = ObjectProperty()


if __name__ == "__main__":
    MobileApp().run()
