# Створiть 3 рiзних функцiї (на ваш вибiр). 
# Кожна з цих функцiй повинна повертати якийсь результат. Також 
# створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє 
# повернутий ними результат та також повертає результат. Таким чином 
# ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3.

def func_1():
    user_name = input("Ваше ім'я?:")
    return user_name

def func_2():
    user_age = input("Ваш вік?:")
    return user_age

def func_3():
    user_city = input("Ваше місто?:")
    return user_city

def func_4():
    my_name = func_1()
    my_age = func_2()
    my_cyti = func_3()
    print(f'My name is {my_name}. I am {my_age}. I live in {my_cyti}')
    
func_4()