def insertionSort(alist):
    for idx in range(1, len(alist)):
        current_value = alist[idx]
        position = idx
        while alist[position - 1] > current_value and position > 0:
            alist[position] = alist[position - 1]
            position = position - 1
        
        alist[position] = current_value
    return alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)
