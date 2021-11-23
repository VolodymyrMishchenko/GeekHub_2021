# Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для роботи захардкодити свій.
dic = {"a": "movies", "x": "music", "p": "movies","r": "sports", "t": "news"}
temp = []
result = dict()
for key, value in dic.items():
    if value not in temp:
        temp.append(value)
        result[key] = value
print(result)