# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї 
# функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати 
# документацію по ній: 
# https://docs.python.org/3/library/stdtypes.html#range

def custom_range(start, stop=0, step=1):
<<<<<<< HEAD
    if step > 0:
        if start and not stop:
            stop = start
            start = 0
        while start < stop:
            yield start
            start += step
    else:
        if start > stop:
            while start > stop:
                yield start
                start += step


     
     
print(list(custom_range(20)))
print(list(custom_range(0, 20)))
print(list(custom_range(0, 20, 2)))
print(list(custom_range(20, 0, -2)))
print(list(custom_range(20, 0)))
print(list(custom_range(-20)))
print(list(custom_range(0, 20, -2)))

print(list(range(0, 20, 2)))
