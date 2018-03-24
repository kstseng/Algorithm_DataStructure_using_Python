def binarySearch(alist, item):
    found = False
    first = 0
    last = len(alist) - 1

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return found

def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint], item)
            else:
                return binarySearchRecursive(alist[(midpoint + 1):], item)



alist = [1, 3, 5, 6, 8]
item = 7
print(binarySearch(alist, item))
print(binarySearchRecursive(alist, item))