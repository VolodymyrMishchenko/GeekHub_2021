# 1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот. 
# Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і 
# кількість). Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот 
# наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром 
# і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти 
# номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ). 
# Особливості реалізації: 
# - перелік купюр: 10, 20, 50, 100, 200, 500, 1000; 
# - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами: 
#       - переглянути наявні купюри; 
#       - змінити кількість купюр; 
#       - видача грошей для користувачів відбувається в межах наявних купюр; 
# - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, 
# що в нього входить, відкладає в окрему касету. 
# 2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль). 
# До того ж, скоріш за все, вам прийдеться і так багато чого переписати.

import json

from datetime import datetime


def transactions(user_name, money):
    data_log = {str(datetime.now()): money}
    with open(f'{user_name}_transactions.json', 'a') as f:
       json.dump(data_log, f)
    return

def get_user(user_name, user_password):
	with open("users.json", "r") as f:
		text = json.load(f)
    	for user_dict in text:
    		if user_name == first_name:
       			return user_name
        	else:
           		print('Не вірний пароль')
           		return False

def get_balance(user_name):
	with open(f'{user_name}.txt') as f:
		balance = f.read()
		return balance
      
def add_cash(user_name):
   cash = abs(int(input("Скільки покласти: ")))
   current_balance = int(get_balance(user_name))
   with open(f'{user_name}.txt', 'w') as f:
      add_balance = current_balance + cash
      f.write(str(add_balance))
      print(f'Ви поклали: {cash}, \nВаш баланс: {add_balance}')
   transactions(user_name, cash)
   return

def withdraw_cash(user_name):
   cash = abs(int(input("Скільки зняти: ")))
   current_balance = int(get_balance(user_name))
   if cash > current_balance:
      print('Недостатньо коштів на балансі')
      
   else:
      with open(f'{user_name}.txt', 'w') as f:
         add_balance = current_balance - cash
         f.write(str(add_balance))
         print(f'Ви зняли: {cash}, \nВаш баланс: {add_balance}')
      transactions(user_name, -cash)
   return
   
def start():
   user_name = get_user(input("Введіть ім'я: "), input("Введіть пароль: "))
   if not user_name:
      print("Такого користувача немає")
      return
   while True:
      menu = int(input("Виберіть операцію: \n1. Вивести баланс \n2. Поповнити баланс \n3. Зняти готівку \n4. Вихід \n"))
      if menu == 1:
         print(get_balance(user_name))
      elif menu == 2:
         add_cash(user_name)
      elif menu == 3:
         withdraw_cash(user_name)
      elif menu == 4:
         return
      else:
         print("Немає такої операції")

start()



