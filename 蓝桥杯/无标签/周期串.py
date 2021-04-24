s = input().strip()
for i in range(1, len(s)//2+1):
    t = set()
    for j in range(0, len(s), i):
        t.add(s[j:j+i])
    if len(t) == 1:
        print(i)
        break
        
            
        
    
