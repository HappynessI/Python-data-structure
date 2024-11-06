# 嵌套列表法表示树

# myTree=['a', # 树根
#         ['b', #左子树
#          ['d',[],[]],
#         ['e',[],[]]],
#         ['c', # 右子树
#         ['f',[],[] ],
#          []]
#         ]
#
# print(myTree)

def BinaryTree(r):  # 创建一个带有根节点的二叉树
    return [r,[],[]]

def insertLeft(root,newBranch):  # 插入左子树
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root


def insertRight(root,newBranch):  # 插入左子树
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
#　这个被注释的用法插入的逻辑是——将新节点插入最深的右节点
# def insertRight(root, newBranch):
#     if root[2]:  # 如果右子树存在
#         insertRight(root[2], newBranch)  # 递归插入到右子树
#     else:
#         root[2] = [newBranch, [], []]  # 创建新的右子树
#     return root

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0]=newVal


r=BinaryTree(3)

insertLeft(r,4)
insertRight(r,5)
insertRight(r,6)
insertRight(r,7)
print(r)
l=getLeftChild(r)
print(l)

setRootVal(1,9)
print(r)
insertLeft(1,11)

print(r)