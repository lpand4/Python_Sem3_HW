# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19  По идее пример не верный, тк у 5 самая маленькая дробная часть(0) => ответ 0.2
def minim(list):
    min_num = list[0] % 1
    for i in list:
        if i % 1 < min_num:
            min_num = i % 1
    return round(min_num, 6)
def maxim(list):
    max_num = list[0] % 1
    for i in list:
        if i % 1 > max_num:
            max_num = i % 1
    return round(max_num, 6)


length_list = int(input("Введите длину списка: "))
user_list = []
for i in range(length_list):
    user_list.append(float(input(f"Введите {i + 1} элемент: ")))
print(user_list)
print(f"Разница равна {maxim(user_list) - minim(user_list)}")
