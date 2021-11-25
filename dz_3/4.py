# Створiть 3 рiзних функцiї (на ваш вибiр). 
# Кожна з цих функцiй повинна повертати якийсь результат. Також 
# створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє 
# повернутий ними результат та також повертає результат. Таким чином 
# ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3.

def printinfo(user_name):
    user_name = input("Ваше ім'я?:")
    return user_name
result = printinfo('user_name')
def printinfo(user_age):
    user_age = input("Ваш вік?:")
    return user_age
result = printinfo('user_age')
def printinfo(user_city):
    user_city = input("Ваше місто?:")
    return user_city
result = printinfo('user_city')

print(result)