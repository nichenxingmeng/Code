def rin_order(node, visit):
    '''逆中序遍历'''
    if not node:
        return
    rin_order(node.rchild, visit)
    visit(node)
    rin_order(node.lchild, visit)

class DepthNode:
    '''带有深度、父节点的节点'''
    def __init__(self, data, depth, parent, lchild = None, rchild = None):
        self.data = data
        self.depth = depth
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild

class DepthSortBiTree:
    '''带有深度、父节点的二叉排序树'''
    def __init__(self):
        self.root = None

    def insert(self, value, node = None, depth = 0):
        if not self.root:
            self.root = DepthNode(value, depth, None)
            return
        if not node:
            node = self.root
        depth += 1
        if value < node.data:
            if not node.lchild:
                node.lchild = DepthNode(value, depth, node)
            else:
                self.insert(value, node.lchild, depth)
        else:
            if not node.rchild:
                node.rchild = DepthNode(value, depth, node)
            else:
                self.insert(value, node.rchild, depth)

def get_digits(n):
    '''获取数字长度'''
    return len(str(n))

def get_parents(node, parents):
    '''获取一个节点的所有父节点'''
    if node.parent:
        parents.append(node.parent)
        get_parents(node.parent, parents)

def sort_tree_print(node):
    '''打印二叉排序树中的某一个节点'''
    res = ""
    parents = []
    # 获取所有父节点
    get_parents(node, parents)
    # 逆序遍历
    for i in range(len(parents) - 1, -1, -1):
        p = parents[i]
        # 计算父节点所占空间
        node_length = 0
        # 有父 -10
        if p.parent:
            node_length += 1
        # 有子 10-
        if p.lchild or p.rchild:
            node_length += 1
        node_length += get_digits(p.data)
        # 画点
        res += "." * node_length
        # 画竖线
        if i > 0:
            # 左右交叉就加竖线，反之用点代替
            if node.data < p.data and node.data > parents[i - 1].data:
                res += "|"
            elif node.data > p.data and node.dara < parents[i - 1].data:
                res += "|"
            else:
                res += "."

    # 有父
    if node.parent:
        res += "|-"
    res += str(node.data)
    # 有子
    if node.lchild or node.rchild:
        res += "-|"
    print(res)

# 10 18 17 15 12 14 13 19 25 23 5 6 8 9 7 3 4 2 1
a = list(map(int, input().split()))
tree = DepthSortBiTree()
# 建树
for i in a:
    tree.insert(i)
# 逆序遍历，打印
rin_order(tree.root, sort_tree_print)