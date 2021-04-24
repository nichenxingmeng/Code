n = int(input().strip())
dp2 = [0 for _ in range(n+1)]
dp3 = [0 for _ in range(n+1)]

i = 0
while dp3[i] < n:
    i += 1
    dp2[i] = dp2[i-1] + i
    dp3[i] = dp3[i-1] + dp2[i-1] + 1

print(i)
