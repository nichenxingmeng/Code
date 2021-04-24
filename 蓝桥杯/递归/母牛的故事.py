m = []
n = input().strip()
while n != '0':
    m.append(n)
    n = input().strip()

'''m_ = [0 for _ in range(55)]
m_[1] = 1
m_[2] = 2
m_[3] = 3
for i in range(4, 55):
    m_[i] = m_[i-1]+m_[i-3]
for i in range(len(m)):
    print(m_[int(m[i])])'''

'''def f(n):
    if n <= 3:
        return n
    else:
        return f(n-1)+f(n-3)

for i in range(len(m)):
    print(f(int(m[i])))'''
