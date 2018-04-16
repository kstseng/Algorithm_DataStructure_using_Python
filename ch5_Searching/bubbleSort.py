def bubbleSort(alist):
    for loc in range(len(alist), 0, -1):
        for i in range(loc - 1):
            if alist[i] > alist[i + 1]:
                tmp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = tmp
    return alist
            
alist=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
bubbleSort(alist)
print(alist)
