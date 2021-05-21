import heapq
import sys

def Pop():
    if not jihe:
        print('empty')
    else:
        ans = heapq.heappop(jihe)
        print('{}+i{}'.format(ans[2], ans[1]))
        print('SIZE = {}'.format(len(jihe)))

def Insert(x):
    heapq.heappush(jihe, x)
    print('SIZE = {}'.format(len(jihe)))

n = int(input().strip())
jihe = []
heapq.heapify(jihe)
for i in range(n):
    tmp = input().strip()
    if tmp == 'Pop':
        Pop()
    else:
        x_ = tmp.index('+')
        x = int(tmp[7:x_])
        y = int(tmp[x_ + 2:])
        Insert([sys.maxsize - x * x - y * y, y, x])