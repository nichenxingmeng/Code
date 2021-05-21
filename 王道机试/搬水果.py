import heapq

n = int(input().strip())
m = list(map(int, input().strip().split()))

heapq.heapify(m)
ans = 0
while len(m) > 0:
    if len(m) > 1:
        a, b = heapq.heappop(m), heapq.heappop(m)
        ans += a + b
        heapq.heappush(m, a + b)
    else:
        a = heapq.heappop(m)
print(ans)
