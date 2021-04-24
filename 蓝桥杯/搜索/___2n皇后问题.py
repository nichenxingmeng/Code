'''
def queen(A, cur=0):  # cur表示当前行数下标，A储存每行有皇后的列的下标
   global count
   if cur == len(A):  # 溢出棋盘边界，跳出递归判断
       print(A)  # 打印位置
       count += 1  # 可能+1
       return 0  # 跳出本次递归
   for col in range(len(A)):  # col表示当前列下标，从第一行到最后一行遍历
       A[cur], flag = col, True  # 存储当前列下标，暂时判定可以放置皇后
       for row in range(cur):  # 遍历前cur行
           if A[row] == col or abs(col - A[row]) == cur - row:  # 判断放置皇后条件，不可放置if语句生效。A[row]==col表示之前已有皇后不可在此列放置，abs(col-A[row])==cur-row对当前行相对于第cur+1行（cur表示下标所以+1）已有皇后的两斜向位置是否可以放置
               flag = False  # 不可以放置皇后
               break  # 跳出for循环
       if flag:  # 判断是否可以放置皇后
           queen(A, cur+1)  # 可以放置皇后进行下一行皇后的判断
count = 0  # 初始化可能数
queen([None]*8)  # 调用递归函数并赋值棋盘最大行
print(count)  # 打印总的可能个数




def black_queen(k):  # 定义黑皇后递归函数，k为行下标
   global count  # 定义全局变量
   for q in range(k - 1):  # 循环遍历前k-1列，判断是否可以放置黑皇后
       judge = b_queen[q] - b_queen[k - 1]  # 第q+1行与第k行列下标差值
       if judge == 0 or k - 1 - q == abs(judge):  # judge == 0重复放置同一列，k - 1 - q == abs(judge)黑皇后位置在同一斜线上
           return  # 此可能性不成立跳出递归
   if k == n:  # 溢出棋盘边界
       count += 1  # 放置皇后可能性+1
       return  # 跳出递归
   for q in range(n):  # 从第一列遍历到最后一列
       if q != w_queen[k] and chessboard[k][q] == 1:  # q != w_queen[k]与白皇后第k+1行列下标相同不可再放置黑皇后，
                                                       # chessboard[k][q] == 1棋盘位置条件位置为1可以放置皇后
           b_queen[k] = q  # 存储当前黑皇后列下标
           black_queen(k + 1)  # 进行下一行皇后的判断递归

def white_queen(k):  # 定义白皇后递归函数，k为行下标
   for p in range(k - 1):  # 循环遍历前k-1列，判断是否可以放置白皇后
       judge = w_queen[p] - w_queen[k - 1]  # 第q+1行与第k行列下标差值
       if judge == 0 or k - 1 - p == abs(judge):  # judge == 0重复放置同一列，k - 1 - q == abs(judge)白皇后位置在同一斜线上
           return  # 此可能性不成立跳出递归
   if k == n:  # 溢出棋盘
       black_queen(0)  # 白皇后放置完成，进行黑皇后放置递归
       return  # 跳出递归
   for p in range(n):  # 从第一列遍历到最后一列
       if chessboard[k][p] == 1:  # chessboard[k][q] == 1棋盘位置条件位置为1可以放置皇后
           w_queen[k] = p  # 存储当前白皇后列下标
           white_queen(k + 1)  # 进行下一行皇后的判断递归

n = int(input())  # 输入n表示棋盘大小
count = 0  # 放置皇后可能性
chessboard = [[] for _ in range(n)]  # 棋盘
for i in range(n):  # 循环得到棋盘位置是否可以放置皇后的条件
   arr = input().split()  # 能否放置皇后
   for j in range(n):  # 循环设置棋盘
       chessboard[i].append(int(arr[j]))  # 对棋盘设置1/0
w_queen = [0 for _ in range(n)]  # 初始化白皇后位置列下标
b_queen = [0 for _ in range(n)]  # 初始化黑皇后位置列下标
white_queen(0)  # 以白皇后为起始进行递归，0为行下标
print(count)  # 打印所有放置皇后的可能数值
'''
from copy import deepcopy
n = int(input().strip())
qipan = []
for i in range(n):
   qipan.append([int(j) for j in input().strip().split()])

hei1 = [0 for _ in range(2*n+1)]
hei2 = [0 for _ in range(2*n+1)]
hei3 = [0 for _ in range(2*n+1)]
a = [0 for _ in range(n+1)]
count = 0
temp = []

def dfs(x):
   global temp, qipan
   if x > n:
      temp_ = deepcopy(qipan)
      for i in range(1, n+1):
         qipan[i-1][a[i]-1] = 0
      temp.append(qipan)
      qipan = deepcopy(temp_)
      return
   for i in range(1, n+1):
      if qipan[x-1][i-1] == 1 and hei1[i] == 0 and hei2[i+x] == 0 and hei3[x-i+n] == 0:
         a[x] = i
         hei1[i] = 1
         hei2[i+x] = 1
         hei3[x-i+n] = 1
         dfs(x+1)
         hei1[i] = 0
         hei2[i+x] = 0
         hei3[x-i+n] = 0

dfs(1)

def dfs_(x):
   global count
   if x > n:
      count += 1
      return
   for i in range(1, n+1):
      if qipan[x-1][i-1] == 1 and bai1[i] == 0 and bai2[i+x] == 0 and bai3[x-i+n] == 0:
         bai1[i] = 1
         bai2[i+x] = 1
         bai3[x-i+n] = 1
         dfs_(x+1)
         bai1[i] = 0
         bai2[i+x] = 0
         bai3[x-i+n] = 0  

count = 0
for i in range(len(temp)):
   qipan = deepcopy(temp[i])

   bai1 = [0 for _ in range(2*n+1)]
   bai2 = [0 for _ in range(2*n+1)]
   bai3 = [0 for _ in range(2*n+1)]

   dfs_(1)
print(count)
   
               
   
