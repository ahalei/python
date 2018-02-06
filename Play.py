import Ball
from Tkinter import * #在不使用模块名字的情况下使用模块的内容
import time
import random
global fx
fx = "s"
global book
book =[[0]*50 for i in range(50)]
def changeFx(event):
    global fx
    if event.keysym == 'Up':
        if fx != 's':
            fx = 'w'
        #print(fx)
    elif event.keysym == 'Down':
        if fx != 'w':
            fx = 's'
        #print(fx)
    elif event.keysym == 'Left':
        if fx != 'd':
            fx = 'a'
        #print(fx)
    else:
        if fx != 'a':
            fx = 'd'
        #print(fx)
        
def food():
    global book
    while 1>0:
        foodx=random.randint(5,25)
        foody=random.randint(5,25)
        if book[foodx][foody]==0 :
            break
    book[foodx][foody]=1
    return foodx, foody
    
    
tk = Tk() #tk对象创建了一个基本的窗口。我们可以在上面增加其他东西，例如按钮，输入框、或者用来画图的画布
tk.title="Aha_Game"
tk.resizable(0,0)#窗口在水平和垂直大小都不能调整
tk.wm_attributes("-topmost",1)#让窗口放到最前面
canvas  = Canvas(tk,width=600,height=600)
canvas.bind_all('<KeyPress-Up>',changeFx)
canvas.bind_all('<KeyPress-Down>',changeFx)
canvas.bind_all('<KeyPress-Left>',changeFx)
canvas.bind_all('<KeyPress-Return>',changeFx)
canvas.bind_all('<KeyPress-Right>',changeFx)
canvas.pack() #pack函数让画布显示在窗口中正确的位置上。如果没有调用这个函数，就不会正常地显示任何东西


snake = []
snake.append(Ball.Ball(canvas, 'blue', 1, 1))
snake.append(Ball.Ball(canvas, 'blue', 1, 2))
snake.append(Ball.Ball(canvas, 'red',  1, 3))
book[1][1]=1
book[1][2]=1
book[1][3]=1


#food
foodx, foody = food()
foodnode = Ball.Ball(canvas, 'green', foodx, foody)


while(1>0):

    #change color
    snake[len(snake)-1].color = 'blue'
    canvas.delete(snake[len(snake)-1].id)
    book[snake[len(snake)-1].x][snake[len(snake)-1].y]=0
    snake[len(snake)-1].draw()
    #add new
    if fx=='s':
        tx =  snake[len(snake)-1].x
        ty =  snake[len(snake)-1].y + 1
    if fx=='w':
        tx =  snake[len(snake)-1].x
        ty =  snake[len(snake)-1].y - 1    
    if fx=='d':
        tx =  snake[len(snake)-1].x + 1
        ty =  snake[len(snake)-1].y
    if fx=='a':
        tx =  snake[len(snake)-1].x - 1
        ty =  snake[len(snake)-1].y  
    
    tx = tx % 30  #防止越界
    ty = ty % 30  #防止越界
    
    if  tx==foodx and ty==foody :
        #food
        canvas.delete(foodnode.id)
        foodx, foody = food()
        foodnode = Ball.Ball(canvas, 'green', foodx, foody)          
    else :
        #delete first
        canvas.delete(snake[0].id)
        book[snake[0].x][snake[0].y]=0
        snake.pop(0)
        
    snake.append(Ball.Ball(canvas, 'red', tx, ty))
    book[tx][ty]=1
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.2)
    
#tk.mainloop()

