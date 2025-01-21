from random import randint

# сортировка пузырьком списка a
def bubbleSort(a):
    n = len(a)
    for q in range(n - 1):
        for i in range(n - q - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

a = [randint(0, 1000) for _ in range(20)] # случайный список на 20 элементов
print(*a)

bubbleSort(a)
print(*a)