s = list(input().strip().split())
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            s[j] = []
while [] in s:
    s.remove([])
print(len(s))
