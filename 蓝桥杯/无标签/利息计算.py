a, b = map(float, input().strip().split())
s = a+(a*b/100*0.8)
print('{:.2f}'.format(s))
