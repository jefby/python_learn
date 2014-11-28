__author__ = 'jefby'
#coding=utf-8

from Tkinter import *
colorIndex = 0
reliefIndex = 0

def changeRelief():
   reliefList = ['flat','raised','sunken','groove','ridge']
   global reliefIndex
   label.config(relief=reliefList[reliefIndex%len(reliefList)])
   reliefIndex += 1

def changeColor(event):
    colorList = ['red','blue','green']
    global colorIndex
    label.config(fg=colorList[colorIndex%len(colorList)])
    colorIndex += 1


#创建主窗体
root = Tk()

label = Label(root,text = "Welcome to python")
button1 = Button(root,text = "relief",command=changeRelief)
#button2 = Button(root,text = "color",command=changeColor)
button2 = Button(root,text = "color")
button2.bind("<Button-1>",changeColor)

#布局
label.pack()
button1.pack(side=LEFT,anchor=CENTER,expand=YES)
button2.pack(side=LEFT,anchor=CENTER,expand=YES)

#创建事件循环
root.mainloop()
