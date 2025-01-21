from random import randint 

l = [randint(0, 100) for _ in range(10)] # список на 10 элементов
print(*l) 
mine = l[0] # предполагаем что мин. елемент - первый
for i in range(1, len(l)): # можно не проверять 0й элемент
    if mine < l[i]:
        mine = l[i] # изменяем мин если нашли больше
print(mine)