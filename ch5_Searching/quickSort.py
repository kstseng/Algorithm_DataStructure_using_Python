def swap(alist, index_i, index_j):
    tmp = alist[index_i]
    alist[index_i] = alist[index_j]
    alist[index_j] = tmp

def partition(alist, front, end):
    pivot = alist[end]
    i = front - 1
    for j in range(front, end):
        if alist[j] < pivot:
            i += 1
            swap(alist, i, j)
    i += 1
    swap(alist, i, end)
    return i

def quickSort(alist, front, end):
    if (front < end):
        pivot = partition(alist, front, end)
        quickSort(alist, front, pivot - 1)
        quickSort(alist, front, pivot - 1)

    return alist

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist, 0, len(alist) - 1)
print(alist)
