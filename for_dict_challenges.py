# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
names = []
for item in students:
    names.append(item["first_name"])
name_dict = {i: names.count(i) for i in names}
for key, value in name_dict.items():
    print(f'{key}: {value}')
print('-------------------\n')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students_2 = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

names_student = []
for item in students_2:
    names_student.append(item["first_name"])
name_dict_ = {i: names_student.count(i) for i in names_student}

for key, value in name_dict_.items():
  if value == max(name_dict_.values()):
    print(f'Самое частое имя среди учеников: "{key}"')

# Пример вывода:
# Самое частое имя среди учеников: Маша
print('-------------------\n')
# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???
class_top_name = []
group = []
names_list = []
for item in school_students:
    class_top_name.append(list(d["first_name"] for d in item))

for group_name in class_top_name:
    names_list.append({i: group_name.count(i) for i in group_name})

count = 0
for d in names_list:
    count += 1
    for key, value in d.items():
        if value == max(d.values()):
            print(f'Самое частое имя в классе {count}: "{key}"')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('-------------------\n')
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
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
# ???

for student in school:
    for key, value in student.items():
        if key == 'students':
            male = 0
            female = 0
            for names in value:
                for k, v in names.items():
                    if is_male[v] == True:
                        male += 1
                    if is_male[v] == False:
                        female += 1
            print(f'В классе {student["class"]}: {female} девочки, и {male} мальчика.')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print('-------------------\n')
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
# ---------------smirnov:  добавил в список школы, больше классов для проверки циклов.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '2г', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '2е', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Валя'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Петр'}, {'first_name': 'Иван'}]},
  {'class': '3а', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Иван'}]},
  {'class': '3д', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
  'Валя': False,
  'Петр': True,
  'Иван': True,
}
# ???

gender_stats = []
female_dict = {}
male_dict = {}

# Заполняем словарь информацией о количестве мальчико и девочек в классе.
for student in school:
    for key, value in student.items():
        if key == 'students':
            male = 0
            female = 0
            for names in value:
                for k, v in names.items():
                    if is_male[v] == True:
                        male += 1
                    if is_male[v] == False:
                        female += 1
            gender_stats.append({'class': student["class"], 'female': female, 'male': male})

#Заполняем два словаря  количеством преобладающего пола учашихся в классе. Для каждого пола свой словарь.            
print(gender_stats)
for gender in gender_stats:
    if gender['female'] > gender['male']:
        print(gender['female'])
        female_dict[gender['class']] = gender.get('female')
    else:
        male_dict[gender['class']] = gender.get('male')
print(female_dict) 
print(male_dict) 


# Выводим информацию
for k, v in female_dict.items():
    if v == max(female_dict.values()):
        print(f'Больше всего девочек в классе: "{k}".')
for k, v in male_dict.items():
    if v == max(male_dict.values()):
        print(f'Больше всего мальчиков в классе: "{k}".')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a