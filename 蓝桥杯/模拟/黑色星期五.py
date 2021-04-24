from calendar import monthrange
year = int(input().strip())
count = 0

for i in range(1, 13):
    a, b = monthrange(year, i)
    if a == 6:
        count += 1
print(count)
