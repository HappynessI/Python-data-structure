class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

# 约瑟夫问题（热土豆问题）的实现
def hotPotato(nameList,num):
    simqueue=Queue()
    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size()>1: # 直到队伍剩下一个人时停止循环
        for i in range(num): # 这个for循环进行num次传递
            simqueue.enqueue(simqueue.dequeue()) # 一次传递
        simqueue.dequeue() # 传递完之后，杀掉队头的那个人
    return simqueue.dequeue()
print(hotPotato(["A",'B','v',"f","e"],7))

# 决策支持问题————打印任务
## 第一步：对问题进行抽象，确定相关的对象和过程（打印任务的属性；打印队列的属性；打印机的属性）
## 第二步：明确过程————生成和提交打印任务（生成概率和打印页数）、实施打印
## 第三步：模拟时间（统一的时间框架）
import random
class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm # 打印速度
        self.currentTask=None #打印任务
        self.timeRemaining=0 # 任务倒计时

    def tick(self): # 打印一秒
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None

    def busy(self): # 打印忙
        if self.currentTask!=None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp=time # 生成时间戳
        self.pages=random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currentTime):
        return currentTime-self.timestamp

def newPrintTask():
    num=random.randrange(1,3)
    if num==2:
        return True
    else:
        return False

def simulation(numSeconds,pagesPerMinute): #模拟
    labprinter=Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]

    for currentSecond in range(numSeconds): # 时间流逝
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)
        if(not labprinter.busy()) and (not printQueue.isEmpty()):
            nextTask=printQueue.dequeue()
            waitingtimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext((nextTask))
        labprinter.tick()

        if len(waitingtimes)>0: # 却把有等待时间数据时才计算平均值
            averageWait=sum(waitingtimes)/len(waitingtimes)
            print(f"Average Wait {averageWait:6.2f} secs {printQueue.size()} tasks remaining")
        else:
            print("No tasks were completed.")
for i in range(10):
    simulation(1800,5)