'''
def quicksort(alist, left, right):
    i = left
    j = right
    flag = alist[(i+j)//2]
    while i <= j:
        while alist[i] < flag:
            i += 1
        while alist[j] > flag:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1
    if left < j:
        quicksort(alist, left, j)
    if right > i:
        quicksort(alist, i, right)
    
list_ = [3,8,4,10,6,7,2,5,9,1]
quicksort(list_, 0, len(list_)-1)
print(list_)
'''
k = int(input().strip())

def find(alist, left, right):
    if left == right:
        return alist[left]
    i = left
    j = right
    flag = alist[(i+j)//2]
    while i <= j:
        while alist[i] < flag:
            i += 1
        while alist[j] > flag:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1
    if k <= j:
        find(alist, left, j)
    elif k >= i:
        find(alist, i, right )
    else:
        find(alist, j+1, i-1)
        
