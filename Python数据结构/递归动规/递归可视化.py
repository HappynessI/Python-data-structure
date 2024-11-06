import turtle

t=turtle.Turtle()

# def drawSpiral(t,lineLen): # 绘制螺线
#     if lineLen>0:
#         t.forward(lineLen)
#         t.right(90)
#         drawSpiral(t,lineLen-5)
#
#
# drawSpiral(t,100)
# turtle.done()

def tree(brance_len):  # 绘制分形树
    if brance_len>5:   # 树干太短不画，即递归结束条件
        t.forward(brance_len) # 绘制树干
        t.right(20) # 右倾斜20度
        tree(brance_len-15)  # 递归调用，画右边的小树，树干减15
        t.left(40)  # 向左回40度，即左倾斜20度
        tree(brance_len-15) # 递归调用，画左边的小树，树干减15
        t.right(20) # 回正
        t.backward(brance_len) # 退回原位置

# t.left(90)
# t.penup()
# t.backward(100)
# t.pendown()
# t.pencolor('green')
# t.pensize(2)
# tree(75)
# t.hideturtle()
# turtle.done()

