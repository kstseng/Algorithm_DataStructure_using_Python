def hashString(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += (pos + 1)*ord(astring[pos])
    ## folding method
    return sum%tablesize

print(hashString('cat', 11))
print(hashString('tat', 11))
print(hashString('tac', 11))

