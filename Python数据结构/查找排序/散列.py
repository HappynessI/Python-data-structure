# 散列表（hash table，又称为哈希表）是一种数据集，其中数据项的存储方式尤其有利于将来快速的查找定位
# 散列表中的每一个存储位置，成为槽（slot），可以用来保存数据项，每个槽有一个唯一的名称

## 散列函数——实现从数据项到存储槽名称的转换的函数   常见的有求余操作
## 完美散列函数——给定一组数据项，如果一个散列函数能把每一个数据项映射到不同的槽中
## 好的散列函数——冲突最少（近似完美）、计算难度低（额外开销小）、充分分散数据项（节约空间）

### 散列函数在信息领域的应用 MD5 SHA

import hashlib

print(hashlib.md5("hello world!".encode()).hexdigest())
print(hashlib.sha1("hello world!".encode()).hexdigest())


#对任意长的数据分部分来计算
m=hashlib.md5()
m.update("hello world!".encode())
m.update("part 2".encode())
m.update("part 3".encode())
print(m.hexdigest())

# 完美散列函数用于数据一致性校验
##加密形式保存密码；防止文件篡改；彩票投注应用

###  散列函数的设计：折叠法
# 基本步骤：1.将数据项按照位数分为若干段；2.再将几段数字相加；3.最后对散列表大小求余，得到散列值
### 有时候会有一个格数反转的步骤（微调）
# 方法2：平方取中法——首先将数据项做平方运算，然后取平方数的中间两位，在对散列表的大小求余

def hash(astring,tablesize):
    sum=0
    for pos in range(len(astring)):
        sum=sum+ord(astring[pos])

    return sum%tablesize


# 冲突解决方案： 向后逐个槽寻找（线性探测）——>改进为：跳跃性探测   【再散列rehashing】
# 还可以将线性探测变为“二次探测” or 不再固定skip的值，而是逐步增加skip的值
# 还可以选择 数据项链 Chaining （将容纳单个数据项的槽扩展为容纳数据项集合）