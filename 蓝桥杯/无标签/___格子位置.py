n = int(input().strip())
i = int(input().strip())
j = int(input().strip())
for x in range(n):
    print(f'({i},{x+1})', end='')
print()

for x in range(n):
    print(f'({x+1},{j})', end='')
print()

if i <= j:
    for x in range(j-i,n):
        print(f'({x+1+i-j},{x+1})', end='')
else:
    for x in range(i-j,n):
        print(f'({x+1},{x+1+j-i})', end='')
print()

x = i
y = j
while x < n and y > 0:
    x += 1
    y -= 1
if j >= n-i+1:
    for a in range(x,y-1,-1):
        print(f'({a},{n-a+y})', end='')
else:
    for a in range(x-1,y,-1):
        print(f'({a},{n-a+x-n})', end='')
    
