from kivy.lang import Builder

from Libs.ux.classlist import ClassesList
from Libs.ux.lists import Lists, RightButton
from Libs.ux.dialogs import card

import kivymd.uix.snackbar as snackbar


class ShowClasses(object):
    _classes_items = None

    def show_classes(self, info_classes):
        # '''
        # :type info_classes: dict;
        # :param info_classes: {
        #     'Name class': ['StudentsList class', 'path/to/avatar']
        # };
        # '''
        if not self._classes_items:
            # Создание списка классов.
            self._classes_list = ClassesList()
            self._classes_items = Lists(
                dict_items=info_classes, flag='three_list_custom_icon',
                right_icons=self.data.right_icons,
                events_callback=self._event_class_item
            )

            button_add_class = Builder.template(
                'ButtonAdd', disabled=False,
                events_callback=self.show_form_create_class
            )
            self._classes_list.add_widget(self._classes_items)
            self._classes_list.add_widget(button_add_class)
            self.add_screens(
                'class_list', self.manager_tab_classes, self._classes_list
            )
        else:
            # Добавляет класс к существующему списку
            # и выводит список на экран.
            self._add_class_item(info_classes)
            self.manager_tab_classes.current = 'class_list'

    def _event_class_item(self, *args):
        # События пункта списка классов.'''

        def end_call():
            self.screen.current = 'root_screen'

        instanse_button = args[0]
        if type(instanse_button) == RightButton:
            name_class, name_event = instanse_button.id.split(', ')
            if name_event == 'startquiz':
                self.screen.current = 'startquiz_class'
                data_class = self.info_classes[name_class]
                call_screen = self.screen.current_screen.children[0]
                call_screen.name_class = name_class
                call_screen.list_class = data_class[0].split('\n')[0]
                call_screen.avatar = data_class[1]
                call_screen.callback = end_call
            elif name_event == 'sets':
                self._show_names_sets(name_class)
        else:
            name_class, name_event = args

    def _show_names_sets(self, name_class):
        # Выводит на экран окно со списком групп.'''

        def get_choice_set(name_set):
            sets_list.dismiss()
            self._add_class_in_set(name_class, name_set)

        if not self.info_sets.__len__():
            snackbar.make(self.data.string_lang_list_sets_empty)
            return
        sets_list = \
            [[name_set, 'accounts'] for name_set in self.info_sets.keys()]
        sets_list = Lists(
            list_items=sets_list, events_callback=get_choice_set,
            flag='single_list_icon'
        )
        sets_list = card(sets_list, self.data.string_lang_add_in_set)

    def _add_class_item(self, info_classes):
        self._classes_items.three_list_custom_icon(info_classes)
