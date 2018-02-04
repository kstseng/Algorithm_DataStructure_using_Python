def toStr(n, base):
    converString = '0123456789ABCDEF'
    if n < base:
        return converString[n]
    else:
        return toStr(n//base, base) + converString[n%base]

if __name__ == '__main__':
    print(toStr(1453, 16))