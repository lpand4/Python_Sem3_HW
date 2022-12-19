# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def multiply(list):
    result_list = []
    if len(list)%2==1:
        result_len = len(list)//2 + 1
    else:
        result_len = len(list)//2

    for i in range(result_len):
        result_list.append(list[i]*list[-(i+1)])
    print(f"Результат {result_list}")

length_list = int(input("Введите длину списка: "))
user_list = []
for i in range(length_list):
    user_list.append(int(input(f"Введите {i + 1} элемент: ")))
multiply(user_list)


