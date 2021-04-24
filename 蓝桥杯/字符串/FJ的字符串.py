n = int(input())
if n <= 26:
    A = 'A'
    for i in range(1,n):
        A = A+chr(ord('A')+i)+A
    print(A)
