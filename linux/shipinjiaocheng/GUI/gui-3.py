__author__ = 'jefby'
#coding=utf-8
'''
使用键盘的Up和Down来控制画布上所绘制的圆的大小
'''

from Tkinter import *
#创建主窗体
root = Tk()
#增加半径
def increaseRadius(event):
    global radius
    canvas.delete("oval")
    if radius < 100:
        radius += 2
    canvas.create_oval(100-radius,100-radius,
                       100+radius,100+radius,tags="oval")
#减少半径
def decreaseRadius(event):
    global radius
    canvas.delete("oval")
    if radius > 2:
        radius -= 2
    canvas.create_oval(100-radius,100-radius,
                       100+radius,100+radius,tags="oval")
#绘制画布
canvas = Canvas(root,bg="white",width=200,height=200)
#绑定Up和Down按键事件
canvas.bind("<Up>",increaseRadius)
canvas.bind("<Down>",decreaseRadius)
#得到控制权
canvas.focus_set()

radius = 50
#绘制圆
canvas.create_oval(100-radius,100-radius,
                   100+radius,100+radius,tags="oval")
#布局
canvas.pack()

#创建事件循环对象
root.mainloop()
