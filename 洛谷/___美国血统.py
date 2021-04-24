def build(L1, R1, L2, R2):
    for i in range(L2, R2+1):
        if b[i] == a[L1]:
            build(L1 + 1, L1 + i -L2, L2, i - 1)
            build(L1 + i - L2 + 1, R1, i + 1, R2)
            print(a[L1])
            return
