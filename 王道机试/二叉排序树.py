'''
class TreeNode:
    def __init__(self, data,leftchild = None, rightchild = None):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

def Insert(root, x, father):
    if not root:
        root = TreeNode(x)
        print(father)
    elif x < root.data:
        root.leftchild = Insert(root.leftchild, x, root.data)
    else:
        root.rightchild = Insert(root.rightchild, x, root.data)
    return root

n = int(input().strip())
m = list(map(int, input().strip().split()))

root = None
for i in range(n):
    root = Insert(root, m[i], -1)
'''

class TreeNode:
    def __init__(self, data,leftchild = None, rightchild = None):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

def Insert(root, x):
    if not root:
        root = TreeNode(x)
    elif x < root.data:
        root.leftchild = Insert(root.leftchild, x)
    else:
        root.rightchild = Insert(root.rightchild, x)
    return root

def PreOrder(root):
    if not root:
        return
    print(root.data, end = ' ')
    PreOrder(root.leftchild)
    PreOrder(root.rightchild)

def InOrder(root):
    if not root:
        return
    InOrder(root.leftchild)
    print(root.data, end = ' ')
    InOrder(root.rightchild)

def PostOrder(root):
    if not root:
        return
    PostOrder(root.leftchild)
    PostOrder(root.rightchild)
    print(root.data, end = ' ')

n = int(input().strip())
m = list(map(int, input().strip().split()))

root = None
for i in range(n):
    root = Insert(root, m[i])

PreOrder(root)
print()
InOrder(root)
print()
PostOrder(root)
