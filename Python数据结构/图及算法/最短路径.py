# 互联网路由器体系
# Dijkstra算法（迭代算法）
from pythonds.graphs import PriorityQueue,Graph,Vertex
import sys
def dijkstra(aGraph,start):
    pq=PriorityQueue()
    for v in aGraph:
        v.setDistance(sys.maxsize)  # 将每个顶点的初始距离设置为一个很大的数，表示未连接到最小生成树中
        v.setPred(None) # 每个顶点的前驱设置为None，表示初始时没有顶点连接到它
    start.setDistance(0) #设置起始顶点start距离为0
    pq.buildHeap([(v.getDistance(),v) for v in aGraph]) # 将所有顶点按照（距离，顶点对象）的形式放入优先队列中，根据距离构建最小堆
    while not pq.isEmpty(): # 主循环：寻找最短路径
        currentVert=pq.delMin()  # 从优先队列中删除并返回距离最小的顶点
        for nextVert in currentVert.getConnections(): # 遍历当前顶点的邻接节点
            newDistance=currentVert.getDistance()+currentVert.getWeight(nextVert)  # 获取从start到 nextVert的距离
            # 检查并更新邻接顶点的距离
            if nextVert in pq and newDistance<nextVert.getDistance():  # 如果nextVert在优先队列中，且newDistance小于nextVert当前的距离
                nextVert.setPred(currentVert)   # 将currentVert设置为nextVert的前驱顶点
                nextVert.setDistance(newDistance)  # 更新nextVert的距离为newDistance
                pq.decreaseKey(nextVert,newDistance) # 在优先队列中更新nextVert的距离，使其重新排序
    return {v.getId(): v.getDistance() for v in aGraph}


buy=[11,11,12,12,13]
fix=[5,6,8,11,18]

def cuculate_price(i,j):
    total=buy[i-1]
    for num in range(j-i):
        total+=fix[num]
    return total
## vi 表示第i年购买一台设备，vj表示一直用到j-1年末
g=Graph()
for i in range(1,7):
    g.addVertex(i)

for i in range(1,6):# i=1,2...5
    for j in range(2,7):
        if i<j:
            g.addEdge(i,j,cuculate_price(i,j))
# 打印图中的边
for v in g:
    for w in v.getConnections():
        print(f"( {v.getId()} , {w.getId()} ) 费用: {v.getWeight(w)}")

print(dijkstra(g,g.getVertex(1)))