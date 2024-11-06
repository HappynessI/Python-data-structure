# 首先将上层N-1个盘片的盘片塔，从开始柱，经由目标柱，移动到中间柱
# 然后将第N个（最大的）盘片，从开始柱，移动到目标柱
# 最后将放置在中间柱的N-1个盘片的盘片塔，经由开始柱，移动到目标柱

# 基本结束条件：1个盘片的移动问题
def moveTower(height,fromPole,withPole,toPole):
    if height>=1:
        moveTower(height-1,fromPole,toPole,withPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height-1,withPole,fromPole,toPole)

def moveDisk(disk,fromPole,toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")

moveTower(5,'#1',"#2","#3")