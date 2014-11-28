__author__ = 'jefby'
#coding=utf-8
#GUI编程示例

#import tkinter
from Tkinter import *
#创建主窗体
root = Tk()
#标签
label = Label(root,text="Welcome to Python")
#画布
canvas = Canvas(root,bg='white')
#按键
button = Button(root,text='Click me')
#pack布局器，默认从上到下，也可自左向右排列
label.pack()
canvas.pack()
button.pack()
#创建事件循环
root.mainloop()
