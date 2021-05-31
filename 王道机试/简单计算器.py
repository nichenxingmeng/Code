def Priority(c):
    if c == '#':
        return 0
    elif c == '$':
        return 1
    elif c == '+' or c == '-':
        return 2
    else:
        return 3

def isdigit(x):
    if x in '0123456789':
        return True
    return False

def GetNumber(str):
    global index
    num = 0
    while isdigit(str[index]):
        num = num * 10 + int(str[index])
        index += 1
    return num

def Calculate(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y

str = input().strip()
index = 0
oper = []
data = []
str += '$'
oper.append('#')
while index < len(str):
    if str[index] == ' ':
        index += 1
    elif isdigit(str[index]):
        data.append(GetNumber(str))
    else:
        if Priority(oper[-1]) < Priority(str[index]):
            oper.append(str[index])
            index += 1
        else:
            y = data.pop(-1)
            x = data.pop(-1)
            data.append(Calculate(x, y, oper.pop(-1)))
print('{:.2f}'.format(data[0]))
