# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.scrollview import ScrollView
#
# from Libs.ux.dialogs import input_dialog
# from Libs.ux.setlist import SetsList
# from Libs.ux.lists import Lists
#
# from kivymd.accordion import MDAccordionItem
# from kivymd.uix.label import MDLabel
# import kivymd.snackbar as Snackbar
#
#
# class NewSet(FloatLayout):
#     pass
#
#
# class CreateSet(object):
#     _new_set = None
#     _class_list_in_set = None
#
#     def create_set(self):
#         def callback(set_name):
#             dialog_set.dismiss()
#             if set_name:
#                 if set_name in self.info_sets:
#                     Snackbar.make(
#                         self.data.string_lang_set_exists.format(set_name)
#                 )
#                     return
#                 self.info_sets[set_name] = []
#                 self._save_data('sets.ini', self.info_sets)
#                 self._show_set(set_name)
#
#         dialog_set = input_dialog(
#             title=self.title, hint_text=self.data.string_lang_name_set,
#             text_button_ok='OK', events_callback=callback
#         )
#
#     def _show_set(self, sets_data):
#         if self.manager_tab_sets.has_screen('sets') and \
#                 not isinstance(sets_data, str):
#             if self.old_info_sets != sets_data:
#                 self._check_new_add_class_in_sets(sets_data)
#                 return
#             else:
#                 # Выводим на экран список групп, если он был ранее создан.
#                 self.manager_tab_sets.current = 'sets'
#                 return
#
#         if not self._new_set:
#             self._new_set = NewSet()
#         if isinstance(sets_data, str):
#             sets_data = {sets_data: []}
#
#         for set_name in sets_data.keys():
#             self._create_accordion_item(set_name, sets_data)
#
#         if not self.manager_tab_sets.current or \
#                 self.manager_tab_sets.current == 'empty_sets_list':
#             self.add_screens(
#                 'sets', self.manager_tab_sets, self._new_set
#             )
#
#     def _create_accordion_item(self, set_name, sets_data):
#         set_item = MDAccordionItem(
#             id=set_name, title=set_name, icon='accounts',
#             background_color=self.data.alpha, title_theme_color='Primary'
#         )
#         scroll = ScrollView(id=set_name)
#         classes_set = self._get_classes_set(sets_data[set_name])
#         scroll.add_widget(classes_set)
#         set_item.add_widget(scroll)
#         self._new_set.ids.set.add_widget(set_item)
#
#     def _add_class_in_set(self, name_class, set_name):
#        # '''Добавляет контакт в группу.'''
#
#        if name_class not in self.info_sets[set_name]:
#            self.info_sets[set_name].append(name_class)
#            self._save_data('sets.ini', self.info_sets)
#            self.info_classes, self.info_sets, self.info_reports, self.info_scores = self._read_data()
#            Snackbar.make(
#                self.data.string_lang_add_class_in_set.format(
#                    name_class, set_name
#                )
#             )
#
#     def _get_class_set(self, classes_set):
#         # '''Возвращает объект MDLabel - "Контактов нет",
#         # если контакты в группе отсутствуют или объект со списком
#         # добавленных в группу контактов.'''
#
#         if not class_set.__len__():
#             return MDLabel(
#                 text=self.data.string_lang_not_classes,
#                 font_style='Headline', halign='center',
#                 theme_text_color='Custom',
#                 text_color=self.data.text_color
#             )
#         else:
#             for class_name in classes_set:
#                 info_classes = {class_name: self.info_classes[class_name]}
#                 if not self._classes_list_in_set:
#                     classes_list = ClassesList()
#                     self._classes_list_in_set = Lists(
#                         dict_items=info_classes, flag='three_list_custom_icon',
#                         right_icons=self.data.right_icons[:1],
#                         events_callback=self._event_class_item
#                     )
#                     classes_list.add_widget(self._classes_list_in_set)
#                 else:
#                     self._classes_list_in_set.three_list_custom_icon(
#                         info_classes
#                     )
#             self._classes_list_in_set = None
#
#             return classes_list
#
#     def _check_new_add_class_in_sets(self, sets_data):
#         # '''Проверяет и добавляет в группу новые контакты, если таковые
#         # были включены в какую-лиюо группу во вкладке "Контакты".'''
#
#         def add_class_list_in_sets():
#             scroll_in_accordion_item = accordion_item.ids.container.children[0]
#             label_not_classes = scroll_in_accordion_item.children[0]
#             scroll_in_accordion_item.remove_widget(label_not_classes)
#             classes_set = self._get_classes_set(sets_data[set_name])
#             scroll_in_accordion_item.add_widget(classes_set)
#
#         for accordion_item in self._new_set.ids.set.children:
#             for set_name in sets_data.keys():
#                 classes_name_in_set = sets_data[set_name]
#                 if set_name == accordion_item.id:
#                     for class_name in classes_name_in_set:
#                         if set_name in self.old_info_sets:
#                             if class_name not in self.old_info_sets[set_name]:
#                                 accordion_content = \
#                                     accordion_item.ids.container.children[0].children[0]
#                                 if type(accordion_content) == classesList:
#                                     classes_list_in_set = \
#                                         accordion_content.children[0]
#                                     info_classes = \
#                                         {class_name: self.info_classes[class_name]}
#                                     classes_list_in_set.three_list_custom_icon(
#                                         info_classes
#                                     )
#                                 else:
#                                     add_class_list_in_sets()
#                         else:
#                             add_class_list_in_sets()
#
#         self.old_info_sets = sets_data