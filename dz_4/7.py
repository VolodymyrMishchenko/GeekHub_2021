# Написати функцію, яка приймає на вхід список і підраховує 
# кількість однакових елементів у ньому.

lst = ["a", "b", "a", "c", "c", "a", "c"]
def list(lst):
    temp=set(lst)
    result={}
    for i in temp:
        result[i]=lst.count(i)
    print(result)
list(lst)
