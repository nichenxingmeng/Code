s = list(input().strip())
list = ['a','e','i','o','u']

flag = False
for i in range(len(s)):
    if s[i] in list:
        flag = True
        print(i+1)
        break
if not flag:
    print(0)
