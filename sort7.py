from random import randint

def bubbleSort(a, cmp, l, r):
    '''
    Общий случай сортировки пузырьком

    @param a - список, в котором будут сортироваться элементы
    @param cmp - функция-компаратор
    @param l - левая граница сортировки (включительно)
    @param r - правая граница сортировки (не включительно)
    '''
    n = r - l # количество элементов в отрезке [l, r)
    for q in range(n - 1):
        for i in range(l, r - q - 1):
            if not cmp(a[i], a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]

# для сортировки по возрастанию
def smaller(a, b):
    return a < b

# для сортировки по убыванию
def greater(a, b):
    return a > b

n = int(input())
a = [randint(1, 100) for _ in range(n)]
print(*a)

third = n // 3 # длина левой и правой части
central = n - 2 * third # длина центральной части

bubbleSort(a, smaller, 0, third) # сортировка первой части по возр
bubbleSort(a, greater, third, third + central) # вторая часть по убыв
bubbleSort(a, smaller, third + central, n) # третья часть по возр
print(*a)