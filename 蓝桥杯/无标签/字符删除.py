str = input().strip()
ch = input().strip()
str = list(str)

while ch in str:
    str.remove(ch)
print(''.join(str))
