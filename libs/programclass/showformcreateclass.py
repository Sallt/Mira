import os
import pickle
import kivymd.uix.snackbar as snackbar
from libs.uix.dialogue import dialog, file_dialog

class ShowFormCreateClass(object):
    _path_to_avatar = False

    def show_form_create_class(self, *args):
        # '''Выводит на экран форму для создания нового контакта.'''

        self.manager_tab_classes.current = 'create_class'
        # <class 'libs.uix.createclass.CreateClass'>
        self._form_create_class = self.manager_tab_classes.current_screen.children[0]

    def choice_avatar_class(self):
        # '''Выводит файловый менеджер для выбора аватара
        # и устанавливает его для создаваемого контакта. '''

        def on_select(path_to_avatar):
            dialog_manager.dismiss()
            if os.path.splitext(path_to_avatar)[1] in [
                    '.png', '.jpg',  '.jpeg', '.gif']:

                path_to_dir_image, name_image = os.path.split(path_to_avatar)
                name_image = '{}{}'.format(
                    os.path.splitext(name_image)[0], '.png'
                )
                new_path_to_avatar = '{}/data/classes/previous/{}'.format(
                    self.directory, name_image
                )
                # create_previous_portrait(path_to_avatar, new_path_to_avatar)
                self._path_to_avatar = new_path_to_avatar
                self._form_create_class.ids.avatar.source = new_path_to_avatar
            else:
                dialog(title=self.title, text=self.data.string_avatar_wrong)

        dialog_manager, file_manager = file_dialog(
            title=self.data.string_lang_select_avatar, path='.',
            filter='files', events_callback=on_select
        )

    def save_info_class(self):
        # '''Сохраняет информацию о новом контакте.'''

        info_classes = self._read_data()[0]

        name_class = self._form_create_class.ids.name_field.text
        studentlist_class = self._form_create_class.ids.stud_list_field.text.split("\n")
        if self._form_create_class.ids.sorted_alphab.active:
            studentlist_class = studentlist_class.sort()
        elif self._form_create_class.ids.sorted_alphab_reverse.active:
            studentlist_class = studentlist_class.sort().reverse()
        # sort_class = self._form_create_class.ids.sort_field.

        if not self._path_to_avatar:
            self._path_to_avatar = 'data/images/avatar_empty.png'
        if name_class == '':
            snackbar.make(self.data.string_lang_input_name_class)
            return
        if studentlist_class == '':
            snackbar.make(self.data.string_lang_input_studentlist_class)
            return
        if name_class in self.info_classes:
            snackbar.make(
                self.data.string_lang_name_class_exists.format(name_class)
            )
            return

        info_classes[name_class] = [
            '{}\n{}'.format(studentlist_class), self._path_to_avatar
        ]
        self._save_data(data=info_classes)
        self.info_classes, self.info_sets = self._read_data()
        class_data = \
            ['{}\n{}'.format(studentlist_class), self._path_to_avatar]
        self.show_classes({name_class: class_data})
        self._clear_form_create_class()

    def _clear_form_create_class(self):
        self._form_create_class.ids.name_field.text = ''
        self._form_create_class.ids.stud_list_field.text = ''
        self._path_to_avatar = False

    def _save_data(self, file='classes.ini', data=None):
        if not data:
            data = {}

        with open('{}/data/classs/{}'.format(
                self.directory, file), 'wb') as file_classes:
            pickle.dump(data, file_classes)

    def _read_data(self):
        with open('{}/data/classes/classes.ini'.format(
                self.directory), 'rb') as file_classes:
            classes_data = pickle.load(file_classes)
        # with open('{}/Data/classes/sets.ini'.format(
        #         self.directory), 'rb') as file_sets:
        #     sets_data = pickle.load(file_sets)

        return classes_data #, sets_data

    def _check_existence_classes(self):
        if not os.path.exists('{}/data/classes'.format(self.directory)):
            os.mkdir('{}/data/classes'.format(self.directory))
        if not os.path.exists('{}/data/classes/previous'.format(self.directory)):
            os.mkdir('{}/data/classes/previous'.format(self.directory))
        if not os.path.exists('{}/data/classes/classes.ini'.format(
                self.directory)):
            self._save_data()
        if not os.path.exists('{}/data/classes/sets.ini'.format(
                self.directory)):
            self._save_data(file='sets.ini')
