def selectionSort(alist):
    for loc in range(len(alist) - 1, 0, -1):
        local_max_idx = 0
        for i in range(1, loc + 1):
            if alist[i] > alist[local_max_idx]:
                local_max_idx = i
        tmp = alist[loc]
        alist[loc] = alist[local_max_idx]
        alist[local_max_idx] = tmp
    
    return alist

                
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)