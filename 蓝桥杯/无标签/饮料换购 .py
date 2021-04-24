n = int(input().strip())
count = n

while n >=3:
    count += n // 3
    n = n // 3 + n % 3

print(count)
