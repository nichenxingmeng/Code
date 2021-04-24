T = int(input().strip())

def dfs():
    global ru, chu, flag, n, stack
    if flag == True:
        return
    if len(chu) == n:
        if chu == [_ for _ in range(1, n + 1)]:
            flag = True
            return
    if ru:
        back = ru[0]
        stack.append(ru[0])
        ru.pop(0)
        dfs()
        stack.remove(back)
        ru.insert(0, back)
        if stack:
            back_ = stack[0]
            chu.append(stack[0])
            stack.pop(0)
            dfs()
            chu.remove(back_)
            stack.insert(0, back_)

            back__ = stack[-1]
            chu.append(stack[-1])
            stack.pop(-1)
            dfs()
            chu.remove(back__)
            stack.append(back__)
    else:
        if stack:
            back_ = stack[0]
            chu.append(stack[0])
            stack.pop(0)
            dfs()
            chu.remove(back_)
            stack.insert(0, back_)

            back__ = stack[-1]
            chu.append(stack[-1])
            stack.pop(-1)
            dfs()
            chu.remove(back__)
            stack.append(back__) 
        
    

while T > 0:
    n = int(input().strip())
    ru = list(map(int, input().strip().split()))
    stack = []
    chu = []
    flag = False
    dfs()
    if not flag:
        print('NO')
    else:
        print('YES')
    
    T -= 1
