for i in range(4000,5*(9**5)+1):
    s = str(i)
    count = 0
    for j in range(len(s)):
        count += int(s[j])**5
    if i == count:
        print(i)

