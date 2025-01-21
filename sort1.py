from random import randint 

l = [randint(0, 100) for _ in range(20)] # список на 20 элементов
print(*l)
lcopy = l # копируем список
n = len(lcopy)
# сортировка пузырьком
for q in range(n - 1):
    for i in range(n - q - 1):
        if lcopy[i] > lcopy[i + 1]:
            lcopy[i], lcopy[i + 1] = lcopy[i + 1], l[i]
print(*lcopy)