from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# 定义问题
problem = LpProblem("0-1_Knapsack_Problem", LpMaximize)

# 定义物品的价值和重量
values = [3, 4, 8, 8, 10]
weights = [2, 3, 4, 5, 9]
max_weight = 20

# 定义变量，x[i] 是二进制变量，表示是否选择第 i 个物品
x = [LpVariable(f"x{i}", cat="Binary") for i in range(len(values))]

# 定义目标函数：最大化总价值
problem += lpSum(values[i] * x[i] for i in range(len(values)))

# 定义约束：总重量不能超过背包的最大承重
problem += lpSum(weights[i] * x[i] for i in range(len(values))) <= max_weight

# 求解问题
problem.solve()

# 输出结果
optimal_value = sum(values[i] * x[i].varValue for i in range(len(values)))
optimal_solution = [x[i].varValue for i in range(len(values))]

print("Optimal value:", optimal_value)
print("Optimal solution:", optimal_solution)


# 五件物品，（2,3），（3,4），（4,8），（5,8），（9,10）
# 背包仅能负重20Kg
# 要求：总价值最高

## 贪心算法不能很好解决问题，选择动态规划

# # 宝物的重量和价值
tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]


# 最大承重
max_w=20

# 初始化二维表格m[(i,w)]
# 表示前i个宝物中，最大重量w的组合，所的到的最大价值
# 当i什么都不取，或w上限为0，价值均为0
m={(i,w):0 for i in range(len(tr))
            for w in range(max_w+1)}

# 逐个填写二维表格
for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        if tr[i]['w']>w:  # 装不下第一个宝物
            m[(i,w)]=m[(i-1,w)]
        else:
            # 不装第i个宝物 与 装第i个宝物，两个情况下取最大值
            m[(i,w)]=max(
                m[(i-1,w)],
                m[(i-1,w-tr[i]['w'])]+tr[i]['v']
            )

print(m[(len(tr)-1,max_w)])

# 第一种算法好理解一点，在二维表格中从左上到右下逐渐计算每一种情况下利益的最大值，只到算到最后一个就是目标函数的最大值
# 这个线性规划仅有一个约束条件


# 第二种是递归+记忆化
tr={(2,3),(3,4),(4,8),(5,8),(9,10)}
max_w=20
m={}  # 初始化记忆化表格m
def thief(tr,w):
    if tr==set()or w==0:   # 递归结束条件——什么都没得选或者最大负重等于0
        m[tuple(tr),w]=0  # 将中间得到的结果在备忘录上记下来
        return 0
    elif(tuple(tr),w) in m:  # 如果在记忆化表格中出现，直接返回，不再递归调用了
        return m[tuple(tr),w]
    else:
        vmax=0   # 目标函数
        for t in tr:
            if t[0]<=w:
                # 逐个从集合中去掉某个宝物，递归调用
                # 选出所以价值中的最大值
                v=thief(tr-{t},w-t[0])+t[1]
                vmax=max(vmax,v)
        m[(tuple(tr),w)]=vmax
        return vmax

print(thief(tr,max_w))
















