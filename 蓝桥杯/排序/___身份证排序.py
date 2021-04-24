import time
start = time.time()

n = int(input().strip())
m = []
for i in range(n):
    m.append(input().strip())

m.sort(key = lambda x: (x[6:14], x), reverse = True)
print(m)
print("\n".join(m))

end = time.time()
print(end - start)
