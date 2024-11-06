# 队列的变体
# 二叉堆Binary Heap 实现优先队列，保持入队和出队的复杂度为O(log n)
# 最小Key排在队首成为最小堆


from pythonds.trees.binheap import BinHeap

bh=BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

# 为了使堆操作能保持在对数水平上，必须采用二叉树结构，用一个非嵌套的列表表示完全二叉树
# 用完全二叉树：叶结点最多只出现在最底层和次底层，而且最底层的叶结点都连续集中在最左边，每个内部节点都有两个子节点，最多可以有一节点例外
# 完全二叉树中，一个节点下标为p，左子节点下标为2p，右子节点下标为2p+1，父节点下标为p/2

# （最小）堆次序：任何一个节点x，其父节点p中的key均小于x中的key，符合“堆”性质的二叉树，其中任何一条最小路径，均是一个已排序数列，根节点key最小
# insert的实现需要上浮操作；delMin方法的实现需要下沉操作，buildHeap也是下沉法

# 二叉堆的排序


