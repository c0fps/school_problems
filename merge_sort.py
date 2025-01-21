def merge(a: list[int], l: int, mid: int, r: int) -> None:
    n1: int = mid - l
    n2: int = r - mid

    L: list[int] = [0] * n1
    R: list[int] = [0] * n2
    for i in range(n1):
        L[i] = a[l + i]
    for i in range(n2):
        R[i] = a[mid + i]

    i : int = 0
    j: int = 0
    k: int = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
    ma = max(a)
    for i in range(ma, 0, -1):
        for j in range(len(a)):
            print(" " if a[j] < i else "#", end="")
        print()
    print()


def mergeSort(a : list[int], l : int, r : int) -> None:
    if r - l == 1:
        return
    mid : int = (l + r) // 2
    mergeSort(a, l, mid)
    mergeSort(a, mid, r)
    merge(a, l, mid, r)


a = list(map(int, input().split()))
ma = max(a)
for i in range(ma, 0, -1):
    for j in range(len(a)):
        print(" " if a[j] < i else "#", end="")
    print()
print()
mergeSort(a, 0, len(a))
print(*a)