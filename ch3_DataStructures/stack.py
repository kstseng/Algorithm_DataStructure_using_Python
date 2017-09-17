'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
'''

from pythonds.basic.stack import Stack
## 3.5
def revstring(mystr):
    mystr_list = list(mystr)

    rev_list = []
    for i in range(len(mystr_list)):
        rev_list.append(mystr_list[-1])
        mystr_list.pop()

    return ''.join(rev_list)


## 3.6 simple balanced parentheses
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open_symbol, close_symbol):
    opens = "([{"
    closes = ")]}"
    return opens.index(open_symbol) == closes.index(close_symbol)


print(parChecker("((()))"))
print(parChecker("((()"))
print(parChecker("([])"))
print(parChecker("([)]"))



