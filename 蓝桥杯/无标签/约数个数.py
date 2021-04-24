n = int(input().strip())
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
print(count)
        
