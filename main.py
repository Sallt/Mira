import os
from tkinter import Button

from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast

from kivy.uix.modalview import ModalView
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, ListProperty, get_color_from_hex
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.clock import Clock
# from kivymd.uix.screen import MDScreen
# from akivymd import *
# from kivy.uix.widget import Widget
# from libs import programdata as data
# from libs.uix.dialogue import dialog
from kivymd.uix.button import MDRectangleFlatButton, MDRectangleFlatIconButton, MDFloatingActionButton
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics.instructions import Canvas
# from kivy.core.image import Image
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import GridLayout
from PIL import Image as Image1

img_size = Image1.open("data/images/rep_8a.jpg").size


class MobileApp(MDApp):

    def __init__(self, **kvargs):
        super(MobileApp, self).__init__(**kvargs)
        Window.bind(on_keyboard=self.events_program)
        # Clock.schedule_once(self._finish_init)

        # self.screen = StartScreen(events_callback=self.events_program)
        self.window = Window
        self.screen = Builder.load_file('libs/uix/kv/startscreen.kv')
        # self.dialog_load_contact = None
        # self.open_exit_dialog = None
        # self.screen_add_groups = None  # kivy.lang.builder.AddContactAddGroups
        # self.data = data
        # self.current_tab = 'classes'
        self.manager_open = False
        self.manager = None

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def build(self):
        self.title = "Опросник Мира"
        self.icon = 'data/images/logo.png'
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.material_style = "M2"
        self.window.size = (360, 740)
        self.items_class = [
            {
                "viewclass": "MDMenuItem",
                "text": f'{i}',
                "callback": self.callback_for_menu_items(i),
            } for i in ["6 Б", "8 A"]]
        self.items_set = [
            {
                "viewclass": "MDMenuItem",
                "text": "Тригонометрия",
                "callback": self.callback_for_menu_items,
            }]
        # return self.load_kv_files()
        # Builder.load_file('libs/uix/kv/startscreen.kv')
        # self.screen = StartScreen()
        # self.manager_tab_classes = self.screen.ids.sm_tab_classes

        # kv = Builder.load_file('libs/uix/kv/startscreen.kv')
        # return Builder.load_file('/Users/olga/PycharmProjects/Mira/libs/uix/kv/startscreen.kv')
        # return kv

        # sm = Manager()
        # sm.add_widget(Screen1(name='empty'))
        # sm.add_widget(Screen2(name='cr_class'))
        return self.screen

    def file_manager_open(self):
        if not self.manager:
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager, select_path=self.select_path)
            self.manager.add_widget(self.file_manager)
            self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True
        self.manager.open()

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager.dismiss()
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device..'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def change_screen(self, scr_name):
        self.root.current = scr_name

    def choose_class(self):
        print("you've tried to choose between unexistent classes !")
        return

    # def  load_kv_files(self):
    #     dir_kv_files = 'libs/uix/kv'

        # for kv_file in os.listdir(dir_kv_files):
        #     # if kv_files == 'bugreporter.kv':
        #     #     continue
        #     Builder.load_file('{}/{}'.format(dir_kv_files, kv_file))

    def show_form_create_class(self):
        self.root.current = "cr_class"
        return

    def show_form_create_set(self):
        self.root.current = "cr_set"

    def choice_avatar_class(self):
        return

    def choice_question_image(self):
        pass

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

    def save_info_class(self):
        return

    def save_question(self):
        pass

    def save_info_set(self):
        pass

    def start_quiz(self):
        pass

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

    def back_screen(self, event):
        # # Менеджер экранов.
        #
        # # Нажата BackKey на главном экране.
        # if event in (1001, 27):
        #     if self.current_tab == 'classes':
        #         if self.manager_tab_classes.current == 'create_class':
        #             if self.manager_tab_classes.has_screen('class_list'):
        #                 self.manager_tab_classes.current = 'class_list'
        #                 self._clear_form_create_class()
        #             else:
        #                 self.manager_tab_classes.current = 'empty_classes_list'
        #         else:
        #             self.exit_program()
        return

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
    # def __init__(self):
    #     menu_items = [
    #         {
    #             "text": f"Item {i}",
    #             "viewclass": "Item",
    #             "height": 54,
    #             "on_release": lambda x=f"Item {i}": self.menu_callback(x),
    #         } for i in range(5)
    #     ]
    #     self.class_menu = MDDropdownMenu(
    #         caller=self.screen.ids.button,
    #         items=menu_items,
    #         width_mult=4,
    #     )
    #     self.set_menu = MDDropdownMenu(
    #         caller=self.screen.ids.button,
    #         items=menu_items,
    #         width_mult=4,
    #     )

    def menu_callback(self, text_item):
        print(text_item)
        self.add_widget(self.class_menu)


class EmptyScreen(FloatLayout):
    image = StringProperty()
    text = StringProperty()
    callback = ObjectProperty()
    disabled = BooleanProperty()


class ShowList(FloatLayout):
    callback = ObjectProperty()
    disabled = BooleanProperty()


class MyImage(Image):
    def get_size_for_notebook(self, **kwargs):
        global img_size
        width, height = (360, 740)
        return 2*width, (img_size[0] * height / width)


class MyScrollView(ScrollView):
    def on_scroll_y(self, instance, scroll_val):
        if scroll_val < 0.05:  # no logic for this number
            box = MDApp.get_running_app().root.ids.notebook_images
            new_image = MyImage()
            box.add_widget(new_image)
            self.scroll_y = new_image.height / box.height


class Report(GridLayout):
    def __init__(self, **kwargs):
        self.rows = 1
        super(Report, self).__init__(**kwargs)


class CreateClass(Screen):
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


class CreateSet(Screen):
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


class QuizCarousel(BoxLayout):
    cl_name = StringProperty()
    set_n = StringProperty()
    image = StringProperty()
    q_text = StringProperty()

    answer_a = StringProperty()
    answer_b = StringProperty()
    answer_c = StringProperty()
    answer_d = StringProperty()
    quiz_canva = ListProperty()
    quest_count = None
    was_run = None

    def parse_set(self):
        if self.was_run == 1:
            self.clear_widgets()
            self.quiz_canva.reverse()
            for ch in self.quiz_canva:
                self.add_widget(ch)
        self.set_n = "Стереометрия"
        self.image = "data/images/tetraedr.png"
        self.q_text = "Сколько граней у тетраедра?"
        self.answer_a = " две"
        self.answer_b = " три"
        self.answer_c = " четыре"
        self.answer_d = " пять"
        self.quest_count = 8

    def scan_class(self):
        # считывание данных
        # + сохранение данных, считанных камерой
        self.next_question()

    def next_question(self):
        self.quest_count = self.quest_count - 1
        self.quiz_canva = []

        if self.quest_count == 0:
            self.quiz_canva = self.children
            self.was_run = 1
            self.clear_widgets()
            box = BoxLayout()
            box.add_widget(MDLabel(text='Вы завершили прохождение теста!', halign='center'))
            self.add_widget(box)
        else:
            self.quiz_canva = self.children
            if self.quest_count > 4:
                self.q_text = "Сколько у тетраедра диагоналей?"
                self.answer_a = " 3"
                self.answer_b = " 4"
                self.answer_c = " 6"
                self.answer_d = " не имеет"
                if self.quest_count == 7:
                    self.q_text = "Сколько оснований имеет тетраедр?"
                    self.answer_a = " 1"
                    self.answer_b = " 2"
                    self.answer_c = "3"
                    self.answer_d = " 4"
                if self.quest_count == 6:
                    self.q_text = "Что лежит в основании тетраедра?"
                    self.answer_a = " четрехугольник"
                    self.answer_b = " пятиугольник"
                    self.answer_c = " треугольник"
                    self.answer_d = " шестиугольник"
            elif self.quest_count > 0:
                self.image = "data/images/tetr.png"
                self.q_text = "Сколько диагоналей у параллелепипеда?"
                self.answer_a = " 3"
                self.answer_b = " 4"
                self.answer_c = " 6"
                self.answer_d = " не имеет"
                if self.quest_count == 4:
                    self.q_text = "Сколько вершин имеет параллелепипед?"
                    self.answer_a = " 4"
                    self.answer_b = " 6"
                    self.answer_c = " 8"
                    self.answer_d = " 12"
                if self.quest_count == 3:
                    self.q_text = "Сколько оснований имеет параллелепипед?"
                    self.answer_a = " 1"
                    self.answer_b = " 2"
                    self.answer_c = " 3"
                    self.answer_d = " 4"
                if self.quest_count == 2:
                    self.q_text = "Из каких геометрических фигур состоит параллелепипед?"
                    self.answer_a = " параллелограммов"
                    self.answer_b = " треугольников"
                    self.answer_c = " пятиугольников"
                    self.answer_d = " трапеций"

            self.clear_widgets()
            self.quiz_canva.reverse()
            for ch in self.quiz_canva:
                self.add_widget(ch)


class WindowManager(ScreenManager):
    pass


class NavDrawer(MDNavigationDrawer):
    events_callback = ObjectProperty()


if __name__ == "__main__":
    MobileApp().run()
