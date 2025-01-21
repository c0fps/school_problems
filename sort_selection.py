from random import randint

# сортировка выбором списка a
def selectionSort(a):
    n = len(a)
    # ищем мин элемент n - 1 раз для отрезка [i, n)
    for i in range(n - 1):
        mini = i # предположим что индекс мин на отрезке - i
        for j in range(i + 1, n):
            if a[j] < a[mini]:
                mini = j # обновляем если нашли меньше
        # меняем i ый элемент на мин на отрезке [i, n)
        a[i], a[mini] = a[mini], a[i]

a = [randint(1, 100) for _ in range(20)]
print(*a)

selectionSort(a)
print(*a)
