n = int(input().strip())
shulie = list(map(int, input().strip().split()))
set_ = set()

for i in range(len(shulie)):
    set_.add(shulie[i])
set_ = list(set_)
set_.sort()
for i in range(len(set_)):
    print(set_[i], shulie.count(set_[i]))
