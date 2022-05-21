import os
import pickle

# from Libs.createpreviousportrait import create_previous_portrait
from Libs.ux.dialogs import dialog, file_dialog, card

import kivymd.uix.snackbar as snackbar


class QuizQuestion(object):
    def __init__(self, text, img, answers):
        self.text = text
        self.img = img
        self.answers = answers


class ShowFormCreateSet(object):
    _path_to_avatar = False

    def __init__(self):
        self.questions = []

    def show_form_create_set(self, *args):
        # '''Выводит на экран форму для создания нового контакта.'''

        self.manager_tab_sets.current = 'create_set'
        # <class 'libs.uix.createset.CreateSet'>
        self._form_create_set = \
            self.manager_tab_sets.current_screen.children[0]

    def choice_question_image(self):
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
                new_path_to_avatar = '{}/Data/sets/previous/{}'.format(
                    self.directory, name_image
                )
                # create_previous_portrait(path_to_avatar, new_path_to_avatar)
                self._path_to_avatar = new_path_to_avatar
                self._form_create_set.ids.avatar.source = new_path_to_avatar
            else:
                dialog(title=self.title, text=self.data.string_avatar_wrong)

        dialog_manager, file_manager = file_dialog(
            title=self.data.string_lang_select_avatar, path='.',
            filter='files', events_callback=on_select
        )

    def save_question(self):
        image_question = self._form_create_set.ids.avatar.source
        text_question = self._form_create_set.ids.question_field.text

        keys = ['A', 'B', 'C', 'D']
        answers = [self._form_create_set.ids.answer_a.text, self._form_create_set.ids.answer_b.text,
                   self._form_create_set.ids.answer_c.text, self._form_create_set.ids.answer_d.text]
        correctness = [self._form_create_set.ids.answer_a_check.active, self._form_create_set.ids.answer_b_check.active,
                       self._form_create_set.ids.answer_c_check.active, self._form_create_set.ids.answer_d_check.active]

        answers_question = dict(keys, dict(answers, correctness))

        self.questions.append(QuizQuestion(text_question, image_question, answers_question))

        self._form_create_set.ids.question_field.text = ''
        self._form_create_set.ids.answer_a.text = ''
        self._form_create_set.ids.answer_b.text = ''
        self._form_create_set.ids.answer_c.text = ''
        self._form_create_set.ids.answer_d.text = ''
        self._form_create_set.ids.avatar.source = 'Data/Img/avatar_empty.png'
        return

    def save_info_set(self):
        # '''Сохраняет информацию о новом контакте.'''

        info_sets = self._read_data()[0]

        name_set = self._form_create_set.ids.name_field.text
        image_question = self._form_create_set.ids.avatar.source
        text_question = self._form_create_set.ids.question_field.text

        keys = ['A', 'B', 'C', 'D']
        answers = [self._form_create_set.ids.answer_a.text, self._form_create_set.ids.answer_b.text, self._form_create_set.ids.answer_c.text, self._form_create_set.ids.answer_d.text]
        correctness = [self._form_create_set.ids.answer_a_check.active, self._form_create_set.ids.answer_b_check.active, self._form_create_set.ids.answer_c_check.active, self._form_create_set.ids.answer_d_check.active]

        answers_question = dict(keys, dict(answers, correctness))

        self.questions.append(QuizQuestion(text_question, image_question, answers_question))

        if not self._path_to_avatar:
            self._path_to_avatar = 'Data/Img/avatar_empty.png'
        if name_set == '':
            snackbar.make(self.data.string_lang_input_name_set)
            return
        if len(self.questions) == 0:
            snackbar.make(self.data.string_lang_input_questions_set)
            return
        if name_set in self.info_sets:
            snackbar.make(
                self.data.string_lang_name_set_exists.format(name_set)
            )
            return

        info_sets[name_set] = ['{}'.format(self.questions)]
        self._save_data(data=info_sets)
        self.info_sets, self.info_classes = self._read_data()
        set_data = \
            ['{}'.format(self.questions)]
        self.show_sets({name_set: set_data})
        self._clear_form_create_set()

    def _clear_form_create_set(self):
        self._form_create_set.ids.name_field.text = ''
        self._form_create_set.ids.question_field.text = ''
        self._form_create_set.ids.answer_a.text = ''
        self._form_create_set.ids.answer_b.text = ''
        self._form_create_set.ids.answer_c.text = ''
        self._form_create_set.ids.answer_d.text = ''
        self._form_create_set.ids.avatar.source = 'Data/Img/avatar_empty.png'
        self._path_t

    def _save_data(self, file='sets.ini', data=None):
        if not data:
            data = {}

        with open('{}/Data/sets/{}'.format(
                self.directory, file), 'wb') as file_sets:
            pickle.dump(data, file_sets)

    def _read_data(self):
        with open('{}/Data/sets/sets.ini'.format(
                self.directory), 'rb') as file_sets:
            sets_data = pickle.load(file_sets)
        with open('{}/Data/sets/classes.ini'.format(
                self.directory), 'rb') as file_sets:
            classes_data = pickle.load(file_sets)

        return sets_data, classes_data

    def _check_existence_sets(self):
        if not os.path.exists('{}/Data/sets'.format(self.directory)):
            os.mkdir('{}/Data/sets'.format(self.directory))
        if not os.path.exists('{}/Data/sets/previous'.format(self.directory)):
            os.mkdir('{}/Data/sets/previous'.format(self.directory))
        if not os.path.exists('{}/Data/sets/sets.ini'.format(
                self.directory)):
            self._save_data()
        if not os.path.exists('{}/Data/sets/classes.ini'.format(
                self.directory)):
            self._save_data(file='classes.ini')
