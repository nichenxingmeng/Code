n = int(input().strip())
m = list(map(int, input().strip().split()))

max_ = 0
max__ = max(m)

for i in range(n): 
    temp = m[i:]+m[:i]
    count = 1
    count_ = 0
    temp_ = 0
    while count <= max__ and count_ < n:
        if temp[temp_%n] == count:
            count = 1
            count_ += 1 
        else:
            count += 1
        temp_ += 1
    if max_ < count_:
        max_ = count_
    
print(max_)
