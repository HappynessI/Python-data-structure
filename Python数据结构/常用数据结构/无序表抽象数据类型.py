# 为了实现无序表的数据结构可以采用链接表的方案，并不要求数据项依次存放在连续的内存空间
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext

temp=Node(83)
print(temp.getData())

# 无序表必须要有对第一个节点的引用信息,无序表的head始终指向链条中第一个节点
class UnorderedList:
    def __init__(self):
        self.head=None
    def add(self,items):
        temp=Node(items)  ##创建了新节点对象
        temp.setNext(self.head)  ## 将新节点的指针指向当前的头结点
        self.head=temp  ## 将头指针更新为temp，新节点成为了链表的头结点

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count

    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found

    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())

mylist=UnorderedList()  ## 注意：mylist对象本身并不包含数据项,head只是对首个节点Node的引用

print(mylist.head)
