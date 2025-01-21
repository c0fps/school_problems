from random import randint 

l = [randint(0, 100) for _ in range(21)] # список на 21 элемент
print(*l)

# сортировка пузырьком
n = len(l) - 1
for i in range(n - 1):
    for j in range(n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

l[0], l[10] = l[10], l[0] # меняем местами мин значение и серединк списка

# сортировка левой части
n = 10
for i in range(n - 1):
    for j in range(n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

# сортировка правой части
n = 10
for i in range(n - 1):
    for j in range(11, 11 + n - i - 1): # берем индексы только правой части
        if l[j] < l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print(*l);