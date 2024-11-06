# 生成树算法如下
# （1）图是否有回路，若无，则图就是生成树；否则转（2）
# （2）删除回路中的一条边，判别式，若有回路继续执行（2）；否则图即为生成树

# 最小生成树：图G的生成树中其权之和为最小的生成树叫最小生成树

# 克鲁斯卡尔算法(Kruskal)
# 把图的边去掉，用一个队列记录边的权重并从小到大排序，然后把边从小到大加回去，直到构成一棵树

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



def Kruskal(graph):
    vnum=graph.vertex_num()
    reps=[i for i in range(vnum)]
    mst,edges=[],[]
    for vi in range(vnum):
        for v,w in graph.out_edges(vi):
            edges.append((w,vi,v))
    edges.sort()
    for w,vi,vj in edges:
        if reps[vi]!=reps[vj]:
            mst.append(((vi,vj),w))
            if len(mst)==vnum-1:
                break
            rep,orep=reps[vi],reps[vj]
            for i in range(vnum):
                if reps[i]==orep:
                    reps[i]=rep
    return mst