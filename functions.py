import json

def load_professions():
    file = open("professions.json")
    profession = json.load(file)
    return profession

def load_students():
    file = open("students.json")
    student = json.load(file)
    return student

def get_student_by_pk(pk):
    students = load_students()
    for student in students:
        if student['pk'] == int(pk):
            return student
    return None

def get_profession_by_title(title):
    professions = load_professions()
    for profession in professions:
        if profession['title'] == title:
            return profession
    return None

def check_fitness(student, profession):
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])
    has = student_skills.intersection(profession_skills)
    lacks = profession_skills.difference(has)
    fit_percent = int(len(has) /(len(profession_skills)/100))
    rez = {'has': has, 'lacks': lacks, 'fit_percent':fit_percent}
    return rez