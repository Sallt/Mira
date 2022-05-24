#мда, гениально
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty

class Class(ObjectProperty):
    def __init__(self, name, img, students):
        self.name = name
        self.avatar = img
        self.students = students
        # студенты - словари с номером карточки и именем студента


class Set(ObjectProperty):
    def __init__(self, name, questions):
        self.name = name
        self.quest = questions


class Question(ObjectProperty):
    def __init__(self, name, img, answers):
        self.name = name
        self.image = img
        self.answers = answers
        # ответы - может tuple? с номером, текстом ответа и корректностью


# просто потому что


class Report(ObjectProperty): # отчёты после прохождения теста
    def __init__(self):
        pass
        # дата прохождения теста
        # имя теста
        # имя класса
        # общий процент успеха класса
        # процент успеха каждого из студентов
        # процент выбранных верных ответов для каждого вопроса


class Scoresheet(ObjectProperty):
    def __init__(self):
        pass
        # не знаю, нуждается ли это в существовании, но может так будет удобнее формировать?

        # для экрана журналов
        # каждый журнал содержит инфу по прохождению конкретным классом тестов за период:
        #    вертикаль: имя класса, общая успешность
        #               список класса, успешность каждого студента
        #    горизонталь: имена сетов, в подзаголовке -  текст каждого из вопросов
        #               под текстом вопроса процент верности ответов на него по классу
        #    содержимое: выбранные каждым студентом ответы на каждый вопрос (буквы, верное - зеленым)