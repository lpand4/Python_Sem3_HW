# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def dvoichnoe(num):
    result = ''
    while num // 2 != 0 or num == 1:
        result += str(num % 2)
        num //= 2
    res = result[::-1]
    print(res)

user_number = int(input("Введите число: "))
dvoichnoe(user_number)