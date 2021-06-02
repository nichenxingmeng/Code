def FastExponentiation(a, b, mod):
    ans = 1
    while b != 0:
        if b % 2 == 1:
            ans *= a
            ans %= mod
        b //  = 2
        a *= a
        a %= mod
    return ans

a, b = map(int, input().strip().split())
print(FastExponentiation(a, b, 1000))
        
