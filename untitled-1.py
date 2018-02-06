
#https://www.cnblogs.com/chengd/articles/7287528.html class 讲解
'''
import Tkinter
tk = Tkinter.Tk()
btn = Tkinter.Button(tk,text="click me",command=hello)
btn.pack()
tk.mainloop()

def hello():
    print('are you ok?')
'''
from Tkinter import * #在不使用模块名字的情况下使用模块的内容
import time
class Ball:
    def __init__(self,canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        
    def draw(self):
        self.canvas.move(self.id,-1,0)
#pass 不做任何事情，一般用做占位语句


def move(Event):
    canvas.move(1,-5,0)#第一个参数是需要移动的对象编号，横移5个px，纵移0个px
    
    

tk = Tk() #tk对象创建了一个基本的窗口。我们可以在上面增加其他东西，例如按钮，输入框、或者用来画图的画布
tk.title="aha game"
tk.resizable(0,0)#窗口在水平和垂直大小都不能调整
tk.wm_attributes("-topmost",1)#让窗口放到最前面
canvas  = Canvas(tk,width=500,height=500)
canvas.pack() #pack函数让画布显示在窗口中正确的位置上。如果没有调用这个函数，就不会正常地显示任何东西

c1 = canvas.create_polygon(10,10,10,60,50,35,fill='red')

for x in range(10) :
    canvas.move(c1,5,0)#第一个参数是需要移动的对象编号，横移5个px，纵移0个px
    tk.update() #重画 更新屏幕上的所有内容
    time.sleep(0.05)

canvas.bind_all('<KeyPress-Return>',move) #第一个参数告诉Tkinter需要监听什么事件，此处需要监听的事件名称叫做KeyPress-Return
ball =  Ball(canvas, 'red')



while(1>0):
    ball.draw()
    tk.update_idletasks
    tk.update()
    time.sleep(0.01)

tk.mainloop()





