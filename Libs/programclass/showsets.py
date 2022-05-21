from kivy.lang import Builder

from Libs.ux.setlist import SetsList
from Libs.ux.lists import Lists, RightButton
from Libs.ux.dialogs import card

import kivymd.uix.snackbar as snackbar


class ShowSets(object):
    _sets_items = None

    def show_sets(self, info_sets):
        # '''
        # :type info_sets: dict;
        # :param info_sets: {
        #     'Name set': ['Number set\nMail set', 'path/to/avatar']
        # };
        # '''
        if not self._sets_items:
            # Создаем список контактов.
            self._sets_list = SetsList()
            self._sets_items = Lists(
                dict_items=info_sets, flag='three_list_custom_icon',
                right_icons=self.data.right_icons,
                events_callback=self._event_set_item
            )

            button_add_set = Builder.template(
                'ButtonAdd', disabled=False,
                events_callback=self.show_form_create_set
            )
            self._sets_list.add_widget(self._sets_items)
            self._sets_list.add_widget(button_add_set)
            self.add_screens(
                'set_list', self.manager_tab_sets, self._sets_list
            )
        else:
            # Добавляет контакт к существующему списку
            # и выводит список на экран.
            self._add_set_item(info_sets)
            self.manager_tab_sets.current = 'set_list'

    def _event_set_item(self, *args):
        # События пункта списка контактов.'''

        def end_call():
            self.screen.current = 'root_screen'

        instanse_button = args[0]
        if type(instanse_button) == RightButton:
            name_set, name_event = instanse_button.id.split(', ')
            if name_event == 'call':
                self.screen.current = 'call_set'
                data_set = self.info_sets[name_set]
                call_screen = self.screen.current_screen.children[0]
                call_screen.name_set = name_set
                call_screen.number_set = data_set[0].split('\n')[0]
                call_screen.avatar = data_set[1]
                call_screen.callback = end_call
            elif name_event == 'classes':
                self._show_names_classes(name_set)
        else:
            name_set, name_event = args

    def _show_names_classes(self, name_set):
        # Выводит на экран окно со списком групп.'''

        def get_choice_class(name_class):
            classes_list.dismiss()
            self._add_set_in_class(name_set, name_class)

        if not self.info_classes.__len__():
            snackbar.make(self.data.string_lang_list_classes_empty)
            return
        classes_list = \
            [[name_class, 'accounts'] for name_class in self.info_classes.keys()]
        classes_list = Lists(
            list_items=classes_list, events_callback=get_choice_class,
            flag='single_list_icon'
        )
        classes_list = card(classes_list, self.data.string_lang_add_in_class)

    def _add_set_item(self, info_sets):
        self._sets_items.three_list_custom_icon(info_sets)
