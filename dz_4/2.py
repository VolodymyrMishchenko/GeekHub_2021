# Написати функцію < bank > , яка працює за наступною логікою: 
# користувач робить вклад у розмірі < a > одиниць строком на < years > 
# років під < percents > відсотків (кожен рік сума вкладу збільшується 
# на цей відсоток, ці гроші додаються до суми вкладу і в наступному 
# році на них також нараховуються відсотки). Параметр < percents > є 
# необов'язковим і має значення по замовчуванню < 10 > (10%). 
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank(cash, years, percents=10):
        for year in range(years):
                income = (cash / 100 *percents)
                cash += income
        return cash
               
                 

cash = int(input('Cash: '))
years = int(input('Years: '))
percents = int(input('Percent: '))
print(bank(cash, years))