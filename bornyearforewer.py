"""

Модуль 4 для домашнего задания к третьему вебинару курса Python Developer

В этом модуле будет запрашиваться год рождения Пушкина до корректного ответа

"""

while True:
    year = int(input("В каком году родился А.С. Пушкин? "))
    if year == 1799:
        print("Верно!!!!")
        break
    else:
        print("Неверно.")