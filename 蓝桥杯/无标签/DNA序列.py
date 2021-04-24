m, n = map(int, input().strip().split())
test = []
for i in range(m):
    test.append(input().strip())   
DNA = ['A', 'C', 'G', 'T']
result = []
for i in range(n):
    DNA_ = [0, 0, 0, 0]
    for j in range(m):
        for k in range(4):
            if DNA[k] != test[j][i]:
                DNA_[k] += 1
    min_ = DNA_[0]
    min__ = 0
    for x in range(1, 4):
        if DNA_[x] < min_:
            min_ = DNA_[x]
            min__ = x
    result.append(DNA[min__])
for x in result:
    print(x, end='')
        
