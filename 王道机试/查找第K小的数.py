while True:
    try:
        n = int(input().strip())
        m = list(map(int, input().strip().split()))
        k = int(input().strip())

        m = list(set(m))

        print(m[k - 1])
    except:
        break