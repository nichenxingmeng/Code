t = int(input())
a = t%60
b = t//60%60
c = t//60//60
print(f'{c}:{b}:{a}')
