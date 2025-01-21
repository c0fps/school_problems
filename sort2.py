from random import randint 

l = [randint(0, 100) for _ in range(20)] # список на 20 элементов
print(*l)
# сортировка пузырьком
n = len(l)
for i in range(n - 1):
    for j in range(n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(*l)