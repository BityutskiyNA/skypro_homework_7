import json


def load_professions():
    """Получаем данные по профессиям из файла professions.json"""
    file = open("professions.json")
    profession = json.load(file)
    return profession


def load_students():
    """Получаем данные по студентам из файла students.json"""
    file = open("students.json")
    student = json.load(file)
    return student


def get_student_by_pk(pk):
    """Проверяем наличие студента с таким номером pk, если студент есть то возвращаемы данные по нему.
    Если студента нет то возвращаем None"""
    students = load_students()
    for student in students:
        if student['pk'] == int(pk):
            return student
    return None


def get_profession_by_title(title):
    """Проверяем наличие профессии с таким наименованием, если профессия есть то возвращаем данные по ней.
    Если профессии нет то возвращаем None"""
    professions = load_professions()
    for profession in professions:
        if profession['title'] == title:
            return profession
    return None


def check_fitness(student, profession):
    """Формируем структуру с данными о том какие навыки изучены студентом, какие нет,
    и насколько он подходит для выбранной профессии"""
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])
    has = student_skills.intersection(profession_skills)
    lacks = profession_skills.difference(has)
    fit_percent = int(len(has) /(len(profession_skills)/100))
    return  {'has': has, 'lacks': lacks, 'fit_percent':fit_percent}