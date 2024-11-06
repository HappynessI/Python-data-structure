# 信息广播问题——单波法、洪水解法（Time To Live）、最小生成树
## 最小生成树算法——Prim算法（贪心）、

from pythonds.graphs import PriorityQueue,Graph,Vertex
import sys

def prim(G,start):
    pq=PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)  # 将每个顶点的初始距离设置为一个很大的数，表示未连接到最小生成树中
        v.setPred(None) # 每个顶点的前驱设置为None，表示初始时没有顶点连接到它
    start.setDistance(0) #设置起始顶点start距离为0
    pq.buildHeap([(v.getDistance(),v) for v in G])  # 将所以顶点按照（距离，顶点对象）的形式放入优先队列中，根据距离构建最小堆
    while not pq.isEmpty(): # 主循环：构建最小生成树
        currentVert=pq.delMin()  # 从优先队列中删除并返回距离最小的顶点
        for nextVert in currentVert.getConnections(): # 遍历当前顶点的邻接节点
            newCost=currentVert.getWeight(nextVert)  # 获取权重
            # 检查并更新邻接顶点的距离
            if nextVert in pq and newCost<nextVert.getDistance():  # 如果nextVer不在优先队列中，且newCost小于nextVert当前的距离
                nextVert.setPred(currentVert)   # 将currentVert设置为nextVert的前驱顶点
                nextVert.setDistance(newCost)  # 更新nextVert的距离为newCost
                pq.decreaseKey(nextVert,newCost) # 在优先队列中更新nextVert的距离，使其重新排序
    return newCost