# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names_dict = {}
for student in students:
    first_name = student['first_name']
    if names_dict.get(first_name) is not None:
        names_dict[first_name] += 1
    else:
        names_dict[first_name] = 1
for k in names_dict:
    print(f'{k}: {names_dict[k]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def get_most_frequent_name(students_arr):
    names_dict = {}
    for student in students_arr:
        first_name = student['first_name']
        if names_dict.get(first_name) is not None:
            names_dict[first_name] += 1
        else:
            names_dict[first_name] = 1
    max_k = ''
    max_count = 0
    for k in names_dict:
        if max_count == 0:
            max_k = k
            max_count = names_dict[k]
        elif names_dict[k] > max_count:
            max_k = k
            max_count = names_dict[k]
    return max_k

most_freq_name = get_most_frequent_name(students)
print(f'Самое частое имя среди учеников: {most_freq_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

i = 0
for group in school_students:
    i += 1
    most_freq_name = get_most_frequent_name(group)
    print(f'Самое частое имя в классе {i}: {most_freq_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def count_male_female(school_class):
    male_count = 0
    female_count = 0
    for student in school_class['students']:
        if is_male[student['first_name']]:
            male_count += 1
        else:
            female_count += 1

    return { 
        'male_count': male_count,    
        'female_count': female_count,    
    }

for s_class in school:
    gender_count = count_male_female(s_class)
    print(f"Класс {s_class['class']}: девочки {gender_count['female_count']}, мальчики {gender_count['male_count']}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

max_dict = {}
for s_class in school:
    gender_count = count_male_female(s_class)
    if max_dict.get('max_male_class') is None or gender_count['male_count'] > max_dict['max_male_count']:
        max_dict['max_male_class'] = s_class['class']
        max_dict['max_male_count'] = gender_count['male_count']
    if max_dict.get('max_female_class') is None or gender_count['female_count'] > max_dict['max_female_count']:
        max_dict['max_female_class'] = s_class['class']
        max_dict['max_female_count'] = gender_count['female_count']
    
if max_dict.get('max_male_class') is not None:
    print(f"Больше всего мальчиков в классе {max_dict['max_male_class']}")
if max_dict.get('max_female_class') is not None:
    print(f"Больше всего девочек в классе {max_dict['max_female_class']}")

