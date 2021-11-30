# На основі попередньої функції створити наступний кусок кода:
# а) створити список із парами ім'я/пароль різноманітних видів 
# (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, користуючись 
# валідатором, перевірить ці дані і надрукує для кожної пари значень 
# відповідне повідомлення, наприклад:
# Name: vasya
# Password: wasd
# Status: password must have at least one digit
------
# Name: vasya
# Password: vasyapupkin2000
# Status: OK

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
    
#validation('bf', 'fg12') #user_name меньше 3
#validation('f' * 52, 'g12') #user_name більше 50
#validation('bfjhh', 'uikuik') #user_password Меньше 8
#validation('bfhgh', 'ukhjjghgtu1') #user_password Має одну цифру
#validation('bfhgf', 'uikuikdfg') #user_password Немає цифр
#validation('bfhgf', 'uikuikdfg1' * 10) #user_password Має більше 20
user_list = [

    ('Roma', 'dfgdf2ffgd'),
    ('Ro', 'dfgdf2ffgd'),
    ('f' * 52, 'g12'),
    ('bfjhh', 'uikuik'),
    ('bfhgf', 'uikuikdfg'),
    ('bfhgf', 'uikuikdfg1' * 10)
    
    ]
for user_tuple in user_list:
    status = ''

    try:

        validation(user_tuple[0], user_tuple[1])
        status = 'OK'
        
    except Exception as err:
        status = err

       
    print(f'Name: {user_tuple[0]} \nPassword: {user_tuple[1]} \nStatus: {status}')
    print()      