n = int(input().strip())
n_ = str(n)
count = 0
for i in range(len(n_)):
    count += int(n_[i])**3
if count == n:
    print("YES")
else:
    print("NO")
