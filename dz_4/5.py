# Написати функцію < fibonacci >, яка приймає один аргумент і виводить 
# всі числа Фібоначчі, що не перевищують його.

def fibonacci(n):
    f1 = 1, f2 = 1
    n = int(input())
    print(f1, f2, end=' ')
    while f2 < n:
        print(f2, end=' ')
        f1, f2 = f2, f1 + f2
fibonacci(n = int(input("Enter number: ")))