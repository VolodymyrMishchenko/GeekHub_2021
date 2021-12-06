# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї 
# функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати 
# документацію по ній: 
# https://docs.python.org/3/library/stdtypes.html#range

def custom_range(start, stop=0, step=1):
    if not stop:
        stop = start
        start = 0
    while True:
        yield start
        start = start + step
        if start > stop or start == stop:
            break
        
print(list(custom_range(0, 20, 2)))
print(list(range(0, 20, 2)))

for i in custom_range(0, 20, 2):
    print(i)