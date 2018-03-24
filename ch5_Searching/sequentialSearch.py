def sequentialSearch(alist, item):
    found = False
    pos = 0
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found
    
print(sequentialSearch([1, 2, 3, 5], 5))