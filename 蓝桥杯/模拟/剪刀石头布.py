a, b = map(int, input().strip().split())
if a == b:
    print(0)
elif a == (b+1)%3:
    print(1)
else:
    print(-1)
