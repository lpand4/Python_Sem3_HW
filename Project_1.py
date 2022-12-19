# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def summ(list):
    result = 0
    for i in range(1, len(list), 2):
        result += list[i]
    print(f"Результат равен {result}")

length_list = int(input("Введите длину списка: "))
user_list = []
for i in range(length_list):
    user_list.append(int(input(f"Введите {i + 1} элемент: ")))
summ(user_list)


