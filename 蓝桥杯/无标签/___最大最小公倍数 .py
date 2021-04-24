from itertools import permutations
n = int(input().strip())

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

max_ = 0
if n <= 10:
    temp = list(permutations([i for i in range(1, n+1)], 3))
    for i in range(len(temp)):
        result1 = temp[i][0] * temp[i][1] // gcd(temp[i][0], temp[i][1])
        result2 = result1 * temp[i][2] // gcd(result1, temp[i][2])
        if result2 > max_:
            max_ = result2
else:
    temp = list(permutations([i for i in range(n-50, n+1)], 3))
    for i in range(len(temp)):
        result1 = temp[i][0] * temp[i][1] // gcd(temp[i][0], temp[i][1])
        result2 = result1 * temp[i][2] // gcd(result1, temp[i][2])
        if result2 > max_:
            max_ = result2
print(max_)
