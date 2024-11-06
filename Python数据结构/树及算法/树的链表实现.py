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

r=BinaryTree('a')
r.insertRight('b')
r.insertLeft('c')
r.getRightChild().setRootVal('hello')
r.getLeftChild().insertRight('d')