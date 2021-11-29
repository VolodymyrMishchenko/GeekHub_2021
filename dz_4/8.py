# Написати функцію, яка буде реалізувати логіку циклічного зсуву 
# елементів в списку. Тобто, функція приймає два аргументи: список і 
# величину зсуву (якщо ця величина додатня - пересуваємо з кінця на 
# початок, якщо від'ємна - навпаки - пересуваємо елементи з початку 
# списку в його кінець).
# Наприклад:
# fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
# fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
 
 
nums = [1, 2, 3, 4, 5]
print(nums)
 
shift(nums, -2)
print(nums)
 
shift(nums, 3)
print(nums)