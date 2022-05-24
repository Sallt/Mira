import os
from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import RiseInTransition
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.carousel import MDCarousel
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.core.window import Window
from kivy.clock import Clock
# from kivymd.uix.screen import MDScreen
# from akivymd import *
from kivy.uix.widget import Widget
# from libs import programdata as data
# from libs.uix.dialogue import dialog
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel


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
        # self.current_tab = 'classes'

    def build(self):
        self.title = "Опросник Мира"
        self.icon = 'data/images/logo.png'
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.material_style = "M2"
        self.window.size = (400, 740)
        # return self.load_kv_files()
        # Builder.load_file('libs/uix/kv/startscreen.kv')
        # self.screen = StartScreen()
        # self.manager_tab_classes = self.screen.ids.sm_tab_classes

        kv = Builder.load_file('libs/uix/kv/startscreen.kv')
        # return Builder.load_file('/Users/olga/PycharmProjects/Mira/libs/uix/kv/startscreen.kv')
        # return kv

        # sm = Manager()
        # sm.add_widget(Screen1(name='empty'))
        # sm.add_widget(Screen2(name='cr_class'))
        return kv

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
    pass


class EmptyScreen(FloatLayout):
    image = StringProperty()
    text = StringProperty()
    callback = ObjectProperty()
    disabled = BooleanProperty()


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


    def parse_set(self):
        self.set_n = "Тригонометрия как она есть"
        self.image = "data/images/tumbleweed.png"
        self.q_text = "Сколько граней у тетраедра?"
        self.answer_a = "-одна-"
        self.answer_b = "-шесть-"
        self.answer_c = "-четыре-"
        self.answer_d = "-три-"
        self.quest_count = 2

    def scan_class(self):
        # считывание данных
        # + сохранение данных, считанных камерой

        self.next_question()

    def next_question(self):
        self.image = "data/images/brush.png"
        self.q_text = "Смесь каких цветов даёт пурпурный оттенок?"
        self.answer_a = "-синий, красный-"
        self.answer_b = "-желтый, зеленый-"
        self.answer_c = "-оранжевый, голубой, розовый-"
        self.answer_d = "-красный, белый, голубой-"
        self.quest_count = self.quest_count - 1

        if self.quest_count == 0:
            # self.return_home()
            self.clear_widgets()
            box = BoxLayout()
            box.add_widget(MDLabel(text='Вы завершили прохождение теста!'))
            self.add_widget(box)
        else:
            renewed = []
            for ch in self.children:
                renewed.append(ch)
            self.clear_widgets()
            renewed.reverse()
            for ch in renewed:
                self.add_widget(ch)

    # def return_home(self):
       # app.change_screen('start')


class WindowManager(ScreenManager):
    pass


class NavDrawer(MDNavigationDrawer):
    events_callback = ObjectProperty()


if __name__ == "__main__":
    MobileApp().run()
