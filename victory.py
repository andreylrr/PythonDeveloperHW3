"""

Модуль 6 для домашнего задания к третьему вебинару курса Python Developer

В этом модуле будут запрашиваться годы рождения нескольких известных людей

"""

famous_people = ["Леонардо да Винчи", "1452", "Христофор Колумба", "1451", "Ленина", "1870",
                 "Цоя", "1962", "Лермонтова", "1814"]

# Леонардо да Винчи - 1452
# Христофор Колумб - 1451
# Ленин - 1870
# Цой - 1962
# Лермонтов - 1814

while True:
    wright_ans = 0
    wrong_ans = 0
    for n in range(0, len(famous_people), 2):
        y_birth = input("Введите год рождения " + famous_people[n] + " ")
        if y_birth == famous_people[n+1]:
            wright_ans += 1
        else:
            wrong_ans += 1
    print("Количество правильных ответов: ", wright_ans)
    print("Количество ошибочных ответов:", wrong_ans)
    print("Процент правильных ответов:", (wright_ans/(wrong_ans+wright_ans))*100)
    print("Процент ошибочных ответов:", (wrong_ans/(wright_ans+wrong_ans))*100)
    y_con = input("Хотите поробовать еще раз? Y/N ")
    if y_con != "Y":
        break

