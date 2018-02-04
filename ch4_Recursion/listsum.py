def listsumOrigin(numList):
    res = 0
    for num in numList:
        res = res + num
    return(res)

def listsumRecursive(numList):
    if len(numList) == 1:
        res = numList[0]
    else:
        res = numList[0] + listsumRecursive(numList[1:])
    return(res)