import functions


if __name__ == '__main__':
    print('Введите номер студента')
    student_pk = input()
    student = functions.get_student_by_pk(student_pk)
    if student == None:
        print('У нас нет такого студента')
        exit(0)
    else:
        print(f'Студент: {student["full_name"]}')
        print(f'Знает: {", ".join(student["skills"])}')
    print(f'Выберите специальность для оценки студента {student["full_name"]}')
    profession_title = input()
    profession = functions.get_profession_by_title(profession_title)
    if profession == None:
        print('У нас нет такой специальности')
    else:
        rez = functions.check_fitness(student, profession)
        print(f'Пригодность {rez["fit_percent"]}%')
        print(f'{student["full_name"]} знает  {", ".join(rez["has"])}')
        print(f'{student["full_name"]} не знает {", ".join(rez["lacks"])}')

