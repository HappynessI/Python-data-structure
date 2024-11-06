class BinaryTree:
    def __init__(self,rootObj,value=0):
        self.key=rootObj       # 保存根节点的数据项
        self.leftChild=None    # 保存指向左右子树的树的引用
        self.rightChild=None
        self.value=value

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t   #完成了插入操作，新节点 newNode 成为了当前节点的左子节点，而原来的左子节点成为了 newNode 的左子节点

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.righttChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key

# 除了根节点以外的每一个节点的数据项就成为了当前节点与父节点之间的权重

# 下面定义了一个字典，存放题目的数据，第一个为购置新设备的价格，第二个为维修费
des_dic={"1":[11,5],"2":[11,6],"3":[12,8],"4":[12,11],"5":[13,18]}
buy=[11,11,12,12,13]
fix=[5,6,8,11,18]

def generate_full_binary_tree(depth):
    if depth<1:
        return None
    root = BinaryTree(0) # 创建树的根节点，将其设置成0
    current_level=[root]  # 保存当前所有节点，最初只包含根节点
    count=0 # 设置一个计数器
    for _ in range(depth):  # 创建剩下的depth-1层树
        next_level=[]  # 用于存放创建的子节点
        for node in current_level:
            node.leftChild=BinaryTree(fix[count])
            node.rightChild=BinaryTree(buy[count])
            next_level.extend([node.leftChild,node.rightChild])
        current_level=next_level
        count+=1
    return root

def print_tree(node, level=0, prefix="Root: "):
    """递归打印二叉树的结构"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.key))  # 缩进根据树的深度调整
        if node.leftChild or node.rightChild:  # 如果存在子节点，则继续打印
            print_tree(node.leftChild, level + 1, "L--- ")
            print_tree(node.rightChild, level + 1, "R--- ")

# 调用 print_tree 打印树的结构
tree_root=generate_full_binary_tree(5)

# print_tree(tree_root)

# 递归计算从当前节点到叶节点的最小路径和
def min_path_sum(node):
    if node is None:
        return float('inf')  # 如果节点为空，返回一个较大的值表示不可达

    # 如果当前节点是叶节点，返回其值并打印
    if node.leftChild is None and node.rightChild is None:
        print(f"达到了叶子节点：{node.key}")
        return node.key

    # 递归计算左、右子树的最小路径和
    left_sum = min_path_sum(node.leftChild)
    right_sum = min_path_sum(node.rightChild)

    # 比较左右子树的路径和，选择较小的路径
    if left_sum < right_sum:
        print(f"在节点 {node.key}，选择左子节点 {node.leftChild.key}，该路径的和为 {left_sum}")
        chosen_sum = left_sum
    elif right_sum < left_sum:
        print(f"在节点 {node.key}，选择右子节点 {node.rightChild.key}，该路径的和为 {right_sum}")
        chosen_sum = right_sum
    else:
        # 当左右子树路径和相等时，可以选择任意一侧，这里我们默认选择左子节点
        print(f"在节点 {node.key}，左右子节点路径和相等，默认选择左子节点 {node.leftChild.key}")
        chosen_sum = left_sum

    # 返回当前节点的值加上选择的路径和
    return node.key + chosen_sum


# 生成树并调用 min_path_sum
tree_root = generate_full_binary_tree(5)
result = min_path_sum(tree_root)
print("最短路径和：", result)

