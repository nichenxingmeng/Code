class TreeNode:
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

root = TreeNode(data)

def PreOrder(root):
    if root == None:
        return

    Visit(root.data)
    PreOrder(root.leftChild)
    PreOrder(root.rightChild)

def InOrder(root):
    if root == None:
        return

    InOrder(root.leftChild)
    Visit(root.data)
    InOrder(root.rightChild)

def PostOrder(root):
    if root == None:
        return

    PostOrder(root.leftChild)
    PostOrder(root.rightChild)
    Visit(root.data)

def Visit(data):
    print(data)

def LevelOrder(root):
    Q = []
    if root:
        Q.append(root)

    while Q:
        current = Q.pop(0)
        Visit()
        if current.leftChild:
            Q.append(current.leftChild)
        if current.rightChild:
            Q.append(current.rightChild)
