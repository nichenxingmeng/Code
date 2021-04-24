n, m, k = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

if n < m:
    ans = []
    for S in range((1 << n) - 1, -1, -1):
        cnt = 0
        temp = [0 for _ in range(k)]
        for i in range(n):
            if cnt >= k:
                break
            if S & (1 << i):
                temp[cnt] = i
                cnt += 1
        if cnt == k:
            ans.append(temp)

    ans_ = []
    for i in range(len(ans)):
        if ans[i] == -1:
            continue
        if ans[i] not in ans_:
            ans_.append(ans[i])
    
    cnt = 0
    for i in range(len(ans_)):
        temp_ = 1

        if k == 1:
            for j in range(len(ans_[i])):
                temp_ *= B.count(A[j])
        else:
            for j in range(len(ans_[i])):
                if A[ans_[i][j]] not in B:
                    temp_ = 0
                    break
                if j >= 1 and B.index(A[ans_[i][j]]) < B.index(A[ans_[i][j-1]]):
                    temp_ = 0
                    break
                else:
                    temp_ *= B.count(A[ans_[i][j]]) 

        cnt += temp_
    print(cnt)

else:
    ans = []
    for S in range((1 << m) - 1, -1, -1):
        cnt = 0
        temp = [0 for _ in range(k)]
        for i in range(m):
            if cnt >= k:
                break
            if S & (1 << i):
                temp[cnt] = i
                cnt += 1
        if cnt == k:
            ans.append(temp)

    ans_ = []
    for i in range(len(ans)):
        if ans[i] == -1:
            continue
        if ans[i] not in ans_:
            ans_.append(ans[i])

    cnt = 0
    for i in range(len(ans_)):
        temp_ = 1

        if k == 1:
            for j in range(len(ans_[i])):
                temp_ *= A.count(B[j])
        else:
            for j in range(len(ans_[i])):
                if B[ans_[i][j]] not in A:
                    temp_ = 0
                    break
                if j >= 1 and A.index(B[ans_[i][j]]) < A.index(B[ans_[i][j-1]]):
                    temp_ = 0
                    break
                else:
                    temp_ *= A.count(B[ans_[i][j]]) 

        cnt += temp_

    print(cnt)
        
                
