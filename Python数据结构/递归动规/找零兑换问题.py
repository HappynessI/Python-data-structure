# 兑换最少个数硬币
# 贪心策略：每次试图解决问题的尽量大的一部分

# def change_greedy(denominations,amount): # denominations——可用的货币面额列表
#     denominations.sort(reverse=True) # 保证面额从大到小排序
#
#     change={} # 储存每种面额的使用数量
#
#     for coin in denominations:
#         if amount>=coin:
#             num=amount//coin # 当前面额需要多少
#             change[coin]=num
#             amount-=num*coin
#
#     if amount!=0:
#         return "无法精确找零"
#
#     return change
#
# denominations=[100,50,20,10,5,1]
# amount=237
# result=change_greedy(denominations,amount)
#
# print(f"找零的方案是:{result}")

# 用递归算法进行计算，确保策略最优（不论币值多么奇怪）
# 基本结束条件：需要兑换的找零，其面值正好等于某种硬币
# 减小问题的规模：每种硬币尝试一次
# def recMC(coinValueList,change):  # 缺点——重复计算太多
#     minCoins=change
#     if change in coinValueList: # 最小规模，直接返回
#         return 1
#     else:
#         for i in [c for c in coinValueList if c <= change]:
#             numCoins=1+recMC(coinValueList,change-i) # 减小规模，每次减去一种硬币面值挑选最小数量
#             if numCoins<minCoins:
#                 minCoins=numCoins
#     return minCoins
# print(recMC([1,5,10,25],63))

# 记忆化递归算法
def recDC(coinValueList,change,knowResults):
    minCoins=change
    if change in coinValueList: # 递归基本结束条件
        knowResults[change]=1 # 记录最优解
        return 1
    elif knowResults[change]>0:
        return knowResults[change] # 查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recDC(coinValueList,change-i,knowResults)
            if numCoins<minCoins:
                minCoins=numCoins # 下一步是找到最优解，记录到表中
                knowResults[change]=minCoins
    return minCoins

print(recDC([1,5,10,35],63,[0]*64))

# 动态规划
def dpMakeChange(coinValueList,change,minCoins,coinUsed):
    for cents in range(1,change+1): # 从1分开始到change逐个计算最少硬币数
        coinCount=cents  # 初始化一个最大值
        newCoin=1  # 初始化新加入的硬币
        for j in [c for c in coinValueList if c<=cents]:  # 减去每个硬币，向后查最少硬币数，同时记录总的最少数
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j # 对应最小数量，所减少的硬币
        minCoins[cents]=coinCount  # 得到当前最少的硬币数，记录到表中
        coinUsed[cents]=newCoin  # 记录本步骤增加的1个硬币
    return minCoins[change] # 返回最后一个结果，循环解释，得到最优解
#
# print(dpMakeChange([1,5,10,21,25],63,[0]*64))


def printCoins(coinUsed,change):
    coin=change
    while coin>0:
        thisCoin=coinUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin

amnt=63
clist=[1,5,10,21,25]
coinUsed=[0]*(amnt+1)
coinCount=[0]*(amnt+1)

print("Making change for",amnt,"requires")
print(dpMakeChange(clist,amnt,coinCount,coinUsed),"coins")
print("They are:")
printCoins(coinUsed,amnt)
print("The used list is as follows:")
print(coinUsed)























