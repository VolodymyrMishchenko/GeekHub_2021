# Маємо рядок --> "f98neroi4nr0c3n30ir5jnpoj35po6j345" -> 
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює 
# наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть 
# букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок 
# без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя

juststring = input()
onlyleters = []
numbersum = 0
numbers = 0
letters = 0

for symbol in juststring:
    if symbol.isdigit():
        numbersum += int(symbol)
        numbers += 1
    elif symbol.isalpha():
        onlyleters += symbol
        letters += 1
if len (juststring) > 30 and len (juststring) < 50:
    print('Довжина рядка',len(juststring))
    print('Кількість цифр',numbers)
    print('Кількість букв',letters)
elif len(juststring) < 30:
    print('Сума чисел:',numbersum)
    print('Рядок без чисел:',''.join(onlyleters))
elif len(juststring) > 50:
    print('Рядок:',juststring[::-1])