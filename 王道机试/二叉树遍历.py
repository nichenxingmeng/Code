class TreeNode:
    def __init__(self, data, leftchild = None, rightchild = None):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

def Build(s):
    global pos
    c = s[pos]
    pos += 1
    if c == '#':
        return
    root = TreeNode(c)
    root.leftchild = Build(s)
    root.rightchild = Build(s)
    return root

def InOrder(root):
    if root == None:
        return
    InOrder(root.leftchild)
    print(root.data)
    InOrder(root.rightchild)

s = list(input().strip())
pos = 0
root = Build(s)
InOrder(root)
