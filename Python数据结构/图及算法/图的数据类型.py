# 由于邻接表的稀疏性，我们可以选择邻接列表来更高效地说明图
## 维护一个包含所有顶点的主列表，主列表中的每个顶点，再关联一个与自身有边连接的所有顶点的列表

class Vertex:  # Vertex数据类型，包含顶点信息、顶点连接边的信息
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}  # 字典存储连接边的信息

# nbr是顶点对象的key  从这个顶点添加一个连接到另一个
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
#顶点数据字符串化，方便打印

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
#返回邻接表中的所有顶点

    def getConnections(self):
        return self.connectedTo.keys()
#返回key
    def getId(self):
        return self.id
#返回顶点边的权重。
    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    # 新加顶点
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # 通过key查找顶点
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:  # 不存在的顶点先添加
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:  #遍历输出
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
