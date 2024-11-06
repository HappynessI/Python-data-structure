# Tree Traversals
# 前序遍历、中序遍历、后序遍历
import operator

class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj       # 保存根节点的数据项
        self.leftChild=None    # 保存指向左右子树的树的引用
        self.rightChild=None

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

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

def postordereval(tree):  # 采用后续遍历重写表达式求值的代码
    opers = {'+': operator.__add__, '-': operator.sub,
            '*': operator.__mul__, '/': operator.__truediv__}
    res1=None
    res2=None
    if tree:
        res1=postordereval(tree.getLeftChild())  # 左子树
        res2=postordereval(tree.getRightChild())  # 右子树
    if res1 and res2:
        return opers[tree.getRootVal()](res1,res2)
    else:
        return tree.getRootVal()

# # 前序遍历——独立的函数实现
# def preorder(tree):
#     if tree:
#         print(tree.getRootVal())
#         preorder(tree.getLeftChild())
#         preorder(tree.getRightChild())

