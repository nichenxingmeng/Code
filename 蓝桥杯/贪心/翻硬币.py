start = list(input().strip())
end = list(input().strip())
count = 0

def fan(x):
    if x == '*':
        return 'o'
    else:
        return '*'

def fanzhuan():
    global start, count
    for i in range(len(start)):
        if start[i] != end[i]:
            start[i] = fan(start[i])
            start[i+1] = fan(start[i+1])
            count += 1

while start != end:
    fanzhuan()
print(count)

