def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0]+listsum(numList[1:])

print(listsum([1,2,3,4,5]))

# 递归三定律
## 1.递归算法必须有一个基本结束条件（最小规模问题的直接解决）
## 2.递归算法必须能改变状态想基本结束条件演进（减小问题规模）
## 3.递归算法必须调用自身（解决减小了规模的相同问题）

# 任意进制转换
## 基本结束条件：余数总小于“进制基base”
## 整数商乘务“更小规模”问题，通过递归调用自身解决

def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base] # 递归拼接字符串

print(toStr(1453,16))

# 当函数被调用的时候，系统会把调用时的现场数据压入到系统调用栈