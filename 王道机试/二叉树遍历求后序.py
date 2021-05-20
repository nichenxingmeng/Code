class TreeNode:
    def __init__(self, data, leftchild = None, rightchild = None):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

def Build(s1, s2):
    if len(s1) == 0:
        return
    c = s1[0]
    root = TreeNode(c)
    pos = s2.index(c)
    root.leftchild = Build(s1[1:pos + 1][:], s2[:pos][:])
    root.rightchild = Build(s1[pos + 1:][:], s2[pos + 1:][:])
    return root

def PostOrder(root):
    if not root:
        return
    PostOrder(root.leftchild)
    PostOrder(root.rightchild)
    print(root.data, end = '')

s1 = list(input().strip())
s2 = list(input().strip())
root = Build(s1, s2)
PostOrder(root)
