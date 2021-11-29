# Написати функцію < prime_list >, яка прийматиме 2 аргументи - 
# початок і кінець діапазона, і вертатиме список простих чисел 
# всередині цього діапазона.

from cmath import sqrt

def is_prime(number):
    
    if number % 2 == 0 and number != 2:
        return False
    
    if number == 0 or number == 1:
        return False
   
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:
            return False
    return True

def prime_list(start, end):
    prime_numbers_list = []
    for number in range(start, end):
        if is_prime(number):
            prime_numbers_list.append(number)
    return prime_numbers_list

begin = int(input('From: '))
finish = int(input('To: '))

print(prime_list(begin, finish))