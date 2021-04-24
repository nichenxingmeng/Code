a = int(input())
b = int(input())
if a >= 0 and b >= 0:
    A = list(str(a))
    A = A[::-1]
    B =list(str(b))
    B = B[::-1]
    r = 0
    C = []
    for i in range(0,min(len(A),len(B))):
        C.append((int(A[i])+int(B[i])+r)%10)
        r = (int(A[i])+int(B[i])+r)//10
    for i in range(min(len(A),len(B)),max(len(A),len(B))):
        if max(len(A),len(B)) == len(A):
            C.append((int(A[i])+r)%10)
            r = (int(A[i])+r)//10
        else:
            C.append((int(B[i])+r)%10)
            r = (int(B[i])+r)//10
    if r > 0:
        C.append(r)
    for i in range(len(C)):
        C[i] = str(C[i])
    print(''.join(C[::-1]))
