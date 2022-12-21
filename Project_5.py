# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

user_number = int(input("Введите число: "))
fib = list(range(user_number * 2 + 1))

fib[1] = 1
fib[0] = 0
fib[-1] = 1
res = []
for i in range(2, user_number + 1):
    fib[-i] = fib[-i + 2] - fib[-i + 1]
    fib[i] = fib[i - 2] + fib[i - 1]
if user_number != 0:
    print(fib[user_number + 1:user_number * 2 + 1:1] + fib[0:user_number + 1:1])
else:
    print(fib[0])


#Если нужен именно массив из чисел, то
# for i in range(user_number+1, user_number * 2 + 1):
#     res.append(fib[i])
# for i in range(user_number+1):
#     res.append(fib[i])
# if user_number != 0:
#   print(res)
# else:
#   print(fib[0])