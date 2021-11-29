# Написати функцію < prime_list >, яка прийматиме 2 аргументи - 
# початок і кінець діапазона, і вертатиме список простих чисел 
# всередині цього діапазона.

def primesList(n):
   
    def is_prime(a):
        if a < 2:
            return False
        return all(a % i for i in xrange(2, a))

    prime_list=[]
    for num in range(2, n +1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list
print(prime_list)