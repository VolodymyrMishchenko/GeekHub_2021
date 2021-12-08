# 1. Програма-банкомат.
# Створити програму з наступним функціоналом:
# - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>)
# - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
# - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
# Особливості реалізації:
# - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
# - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
# - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
# Особливості функціонала:
# - за кожен функціонал відповідає окрема функція;
# - основна функція - <start()> - буде в собі містити весь workflow банкомата:
# - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
# - потім - елементарне меню типа:
# Введіть дію:
# 1. Продивитись баланс
# 2. Поповнити баланс
# 3. Вихід
# - далі - фантазія і креатив :)


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
      if (user_name, user_password) in text.items():
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
