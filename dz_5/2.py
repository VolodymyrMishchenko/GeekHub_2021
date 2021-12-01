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
        raise Exception('user_name має меньше 3 символів')
    if len(user_name) > 50:
        raise Exception('user_name має більше 50 символів')

    if len(user_password) < 8:
        raise Exception('user_password має меньше 8 символів')

    else:
        has_number=False

        for char in user_password:
            if char.isdigit():
                has_number=True
                break
        if has_number is False:
            raise Exception('user_password немає цифр')
        

    if len(user_password) > 20:
        raise Exception('user_password має більше 20 символів')