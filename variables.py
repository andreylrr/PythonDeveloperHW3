import datetime

"""

Модуль 1 для домашнего задания к третьему вебинару курса Python Developer

В этом модуле будет описан объект ИГРУШКА с помощью средств Python

"""

# Название игрушки
name = str("кукла")
# Вес грушки в кг
weight = 0.5
# Является ли эта игрушка детской
is_for_kids = True
# Рекомендуем возраст детей
kids_age = 3
# Дата производства
manufacturing_date = datetime.date(2019, 10, 5)

print("Тип переменной name - ", type(name), sep="")
print("Тип переменной weight - ", type(weight), sep="")
print("Тип переменной is_for_kids - ", type(is_for_kids), sep="")
print("Тип переменной kids_age - ", type(kids_age), sep="")
print("Тип переменной manufacturing_date - ", type(manufacturing_date), sep="")

