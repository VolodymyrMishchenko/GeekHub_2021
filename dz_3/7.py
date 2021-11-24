# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б 
# приймала 3 аргументи - один з яких операцiя, яку зробити!

while True:
    s = input("Введіть операцію (+, -, *, /): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        y = float(input("y = "))
        if s == '+':
            print("%.2f" % (x + y))
        elif s == '-':
            print("%.2f" % (x - y))
        elif s == '*':
            print("%.2f" % (x * y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("Ділення на нуль!")
    else:
        print("Невірний знак операції!")
