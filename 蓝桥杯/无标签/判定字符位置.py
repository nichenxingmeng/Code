s = input().strip()

yuanyin = ['a','e','i','o','u']
flag = False
for i in range(len(s)):
    if s[i] in yuanyin:
        print(i+1)
        flag = True
        break
if not flag:
    print(0)
