# 程序设计语言的编译——词法、语法检查；从语法树生成目标代码
# 自然语言处理——机器翻译、语义理解
# 表达式解析——全括号表达式要分解为单词Token列表，单词分为括号“()”、操作符"+-*/"和操作数"0~9"这及类，左括号就是表达式的开始，右括号是表达式的结束

# (3+(4*5))
# ['(','3','+','(','4','*','5',')',')']
# 创建的关键在于对当前节点的跟踪
## 用一个栈来记录跟踪父节点

# 流程：从全括号表达式到表达式解析树再对表达式进行求值，最后从表达式树中生成全括号表达式
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

class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)  # 入栈下降
    currentTree=eTree
    for i in fplist:
        if i =="(":   # 表达式开始
            currentTree.insertLeft('')
            pStack.push(currentTree)  # 入栈下降
            currentTree=currentTree.getLeftChild()
        elif i not in ["+","-","*","/",")"]:   # 操作数
            currentTree.setRootVal(int(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in ["+","-","*","/"]:   # 操作符
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
        elif i ==")":             # 表达式结束
            currentTree=pStack.pop()   # 出栈上升
        else:
            raise ValueError
    return eTree

# 求值递归函数evaluate的递归三要素
# 基本结束条件：叶节点是最简单的子树，，没有左右子节点，其根节点的数据项即为子表达式树的值
# 缩小规模：将表达式树分为左子树、右子树，即为缩小规模
# 调用自身，分别调用evaluate 计算左子树和右子树的值，然后将左右子树的值依根节点的操作符进行计算，从而得到表达式的值

# 增加可读性：函数引用
import operator
op=operator.__add__   # 将operate.add赋值给一个函数变量
n=op(1,2)
print(n)

def evaluate(parseTree):
    opers={'+':operator.__add__,'-':operator.sub,
           '*':operator.__mul__,'/':operator.__truediv__}   # 将四则运算符映射到对应的Python运算符函数

    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRightChild()   # 缩小规模，递归计算左右子树

    if leftC and rightC:    # 判断是否为操作符节点，如果是，需要进一步计算左右子树的值
        fn=opers[parseTree.getRootVal()]   # 动态选择运算
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()  # 基本结束条件：当前节点没有左右子节点，说明这是一个叶结点，直接返回值

def printexp(tree):
    sVal=""
    if tree:
        sVal='('+printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        sVal=sVal+printexp(tree.getRightChild())+")"
    return sVal
