from random import randint 

l = [randint(0, 100) for _ in range(10)] # список на 10 элементов
print(*l) 
maxe = l[0] # предполагаем что макс. елемент - первый
for i in range(1, len(l)): # можно не проверять 0й элемент
    if maxe < l[i]:
        maxe = l[i] # изменяем макс если нашли больше
print(maxe)