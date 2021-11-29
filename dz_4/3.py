# Написати функцию < is_prime >, яка прийматиме 1 аргумент - число 
# від 0 до 1000, и яка вертатиме True, якщо це число просте, и False 
# - якщо ні.

from cmath import sqrt


def is_prime(number):
    # Все четные числа кроме 2 непростые
    if number % 2 == 0 and number != 2:
        return False
    # 0 и 1 не являются простыми
    if number == 0 or number == 1:
        return False
    # Перебираем числа от 3 до корня из введенного, шаг - 2
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  # Если число делится нацело, то оно непростое
            return False
    return True  # Остальные числа простые

n = int(input('Введите число: '))
print(is_prime(n))