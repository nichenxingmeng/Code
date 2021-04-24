n = str(input().strip())
from itertools import permutations
ans = list(permutations(n))
ans.sort()
temp = 0
for i in range(len(ans)):
    if ans[i] != temp:
        print(''.join(ans[i]))
        temp = ans[i]
