# Створіть функцію, всередині якої будуть записано список із п'яти 
# користувачів (ім'я та пароль). Функція повинна приймати три 
# аргументи: два - обов'язкових (<username> та <password>) і 
# третій - необов'язковий параметр <silent> (значення за замовчуванням
#  - <False>).
# Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True> - 
# функція вертає <False>, інакше (<silent> == <False>) - породжується 
# виключення LoginException

class LoginException(Exception):
    pass

def check_user(username, password, silent=False):
    users = [
        {'bob': '2593'}, 
        {'mell': '4827'}, 
        {'rece': '1597'}, 
        {'kap': '3596'}, 
        {'dax': '4268'}]
    for user in users:
        for name, pas in user.items():
            if username == name and password == pas:
                return True
            elif silent:
                return False
            else:
                raise LoginException('Exceptions')
print(check_user())


    