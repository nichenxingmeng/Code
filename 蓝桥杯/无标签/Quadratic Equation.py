import math
a, b, c = map(float, input().strip().split())
delta = b*b-4*a*c
if delta >= 0:
   x1 = (-b+math.sqrt(delta))/(2*a)
   x2 = (-b-math.sqrt(delta))/(2*a)
   print('{:.2f} {:.2f}'.format(max(x1, x2),min(x1, x2)))
else:
   print('无解')
