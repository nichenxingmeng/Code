x1, y1 = map(int, input().strip().split())
x2, y2 = map(int, input().strip().split())

if x2 - x1 == 0:
    print('INF')
else:
    k = (y2 - y1) // (x2 - x1)
    print(k)
