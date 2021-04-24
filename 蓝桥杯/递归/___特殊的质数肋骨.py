from math import sqrt

n = int(input().strip())

num = [Trie if i%1 else False for i in range(10**n)]
num[2] = True
for i in range(2, int(sqrt(10**n-1))+1):
    j = i
    if num[i]:
        while i*j <= 10**n-1:
            num[i*j] = False
            j += 1

def prime(n):
    if num[i]:
        return True
    else:
        return False

count = 0
def panduan(n, c):
    global count
    if count == c-1:
        print(n)
        return
    for i in range(1, 10):
        nu = n*10 + i
        if prime(nu):
            count += 1
            panduan(nu, c)
            count -= 1

panduan(2, n)
panduan(3, n)
panduan(5, n)
panduan(7, n)
