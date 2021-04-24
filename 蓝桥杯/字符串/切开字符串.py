n = int(input())
s = input().strip()

def huiwen(A):
    A_ = A[::-1]
    if A_ == A:
        return True

def countA(A):
    count = 0
    m = []
    for i in range(1, len(A)+1):
        if i&1:
            temp = len(A)-i+1
            for j in range(0,temp):
                if huiwen(A[j:j+i]):
                    if A[j:j+i] not in m:
                        m.append(A[j:j+i])
                        count += 1
    #print(m)
    return count

def countB(B):
    count = 0
    m = []
    for i in range(1, len(B)+1):
        if i&1:
            temp = len(B)-i+1
            for j in range(0,temp):
                if not huiwen(B[j:j+i]):
                    if B[j:j+i] not in m:
                        m.append(B[j:j+i])
                        count += 1
        else:
            temp = len(B)-i+1
            for j in range(0,temp):
                if B[j:j+i] not in m:
                    m.append(B[j:j+i])
                    count += 1
    return count

max_ = 0
for i in range(1, n):
    A = s[:i]
    count1 = countA(A)
    B = s[i:]
    count2 = countB(B)
    if count1 * count2 > max_:
        max_ = count1 * count2
print(max_)
