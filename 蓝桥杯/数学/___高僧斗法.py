s = list(map(int, input().strip().split()))
m = [0 for x in range(len(s)-1)]
for i in range(0,len(s)-1):
    m[i] = s[i+1]-s[i]-1
count = 0
for i in range(0, len(s)-1, 2):
    count ^= m[i]
if count == 0:
    print(-1)
else:
    for i in range(len(s)-1):
        j = 1
        while True:
            if s[i]+j >= s[i+1]:
                break
            m[i] -= j
            if i != 0:
                m[i-1] += j
            sum_ = 0
            for k in range(0, len(s)-1, 2):
                sum_ ^= m[k]
            if sum_ == 0:
                print(s[i], s[i]+j)
                break
            m[i] += j
            if i != 0:
                m[i-1] -= j
            j += 1
