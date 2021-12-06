# Програма-світлофор. 
# Створити програму-емулятор світлофора для авто і пішоходів. 
# Після запуска програми на екран виводиться в лівій половині - 
# колір автомобільного, а в правій - пішохідного світлофора. 
# Кожну секунду виводиться поточні кольори. Через декілька 
# ітерацій - відбувається зміна кольорів - логіка така сама як 
# і в звичайних світлофорах.


import time

cars_colors = ['Red', 'Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Green', 'Green', 'Green', 'Green']
people_colors = ('Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red')


while True:
    for i in range(len(cars_colors)):
        print(cars_colors[i], people_colors[i])
        time.sleep(1)
