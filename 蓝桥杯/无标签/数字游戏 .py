'''
n, k, t = map(int, input().strip().split())

t_ = 1
count = 1
sum_ = 1
count_ = 1
ans = 1
while t_ < t:
    sum_ += count
    count += 1
    sum_ = sum_ % k
    count_ += 1
    if count_ % n == 1:
        t_ += 1
        ans += sum_

print(ans)
'''

n, k, t = map(int, input().strip().split())

t_ = 1
count = 1
sum_ = 1
count_ = 1
ans = 1
while t_ < t:
    sum_ += (count + count + n - 1)*n//2
    count += n 
    sum_ = sum_ % k
    t_ += 1
    ans += sum_

print(ans)
