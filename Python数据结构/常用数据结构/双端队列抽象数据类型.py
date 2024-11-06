class Deque():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

# 回文词判定
## 将需要判定的词从队为加入deque，再从两端同时移除字符判定是否相同，直到deque中剩下0个或1个字符
def palchecker(aString):
    chardque=Deque()

    for ch in aString:
        chardque.addRear(ch)
    stillEqual=True

    while chardque.size()>1 and stillEqual:
        first=chardque.removeFront()
        last=chardque.removeRear()
        if first!=last:
            stillEqual=False

    return stillEqual
print(palchecker("isasd"))
print(palchecker(("raar")))