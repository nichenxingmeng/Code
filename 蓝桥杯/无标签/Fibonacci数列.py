n = int(input())
F1 = 1
F2 = 2
for i in range(3,n):
    F1, F2 = F2, F1+F2
print(F2%10007)
