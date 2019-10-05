"""

Модуль 5 для домашнего задания к третьему вебинару курса Python Developer

В этом модуле будет запрашиваться год и день рождения Пушкина до корректного ответа

"""
is_end_loop = False
while True:
    year = int(input("В каком году родился А.С. Пушкин? "))
    if year == 1799:
        while True:
            day = int(input("Введите его день рождения по новому стилю в формате ММДД  "))
            if day == 606:
                print("Верно!!!!")
                is_end_loop = True
                break
            else:
                print("Неверный день рождения.")
    else:
        print("Неверный год рождения.")
    if is_end_loop:
        break

