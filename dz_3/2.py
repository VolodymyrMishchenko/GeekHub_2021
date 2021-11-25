# Користувачем вводиться початковий і кінцевий рік. Створити цикл, 
# який виведе всі високосні роки в цьому проміжку (границі включно).

from_year = int(input("Введите год от: "))
to_year = int(input("Введите год до: "))
for year in range(from_year, to_year + 1):
    if year % 400 == 0:
        print("%d високосный" %year)
    elif year % 100 == 0:
        print("%d не високосный" %year)
    elif year % 4 == 0:
        print("%d високосный" %year)
    else:
        print("%d не високосный" %year)