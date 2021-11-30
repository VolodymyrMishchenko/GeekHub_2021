# Створіть функцію для валідації пари ім'я/пароль за наступними 
# правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б 
# одну цифру;
# - щось своє :)
# Якщо якийсь із параментів не відповідає вимогам - породити 
# виключення із відповідним текстом.

def validation(user_name, user_password):
    if len(user_name) < 3:
        raise Exception('Меньше 3')
    if len(user_name) > 50:
        raise Exception('Більше 50')

    if len(user_password) < 8:
        raise Exception('Меньше 8')

    if len(user_password) > 20:
        raise Exception('Більше 20')
    
validation('bfghd', '16216')
