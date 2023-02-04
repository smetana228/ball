

from tkinter import *
import random
from tkinter import messagebox
import time
import datetime
now = datetime.datetime.now()
tk = Tk()


tk.resizable(False, False)
canvas = Canvas(tk, width=400, height=600, bd=0, highlightthickness=0)#КАНВАС
canvas.pack()
tk.title("BALLWAR")

def game(o,o_):
    fin = PhotoImage(file="1560231201_2.png")
    canvas.create_image(200, 300, image=fin)
    class Bruh:#1-платформа
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(125,10,25,25,fill=color)#форма платфромы
            self.canvas.move(self.id, 200,500)#место появления платформы
            self.x = 0
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)#клавиша(налево)
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)#клавиша(направо)
        def draw__(self):#ключ
            self.canvas.move(self.id, self.x, 0)#движение
            pos = self.canvas.coords(self.id)#координаты

            if pos[0] <= 0: #ударение о правый край
                self.x = 2
            elif pos[2] >= self.canvas_width:
                self.x = -2

            if pos[2] >= self.canvas_width: #ударение о левый край
                self.x = -2
            elif pos[0] <= 0:
                self.x = 2

        def turn_left(self, evt):
                self.x = -4 #скорость движения налево
        def turn_right(self, evt):
                self.x = 4 #скорость движения направо


    class Hey:#2-платформа
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(125, 10, 25, 25, fill=color)#форма платфромы
            self.canvas.move(self.id, 200, 50)#место появления платформы
            self.x = 0
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('<KeyPress-a>', self.turn_left)#клавиша(налево)
            self.canvas.bind_all('<KeyPress-d>', self.turn_right)#клавиша(направо)
        def draw_(self):#ключ
            self.canvas.move(self.id, self.x, 0)#движение
            pos = self.canvas.coords(self.id)#координаты
            if pos[0] <= 0: #ударение о левый край
                self.x = 2

            elif pos[2] >= self.canvas_width:
                self.x = -2

            if pos[2] >= self.canvas_width: #ударение о правый край
                self.x = -2
            elif pos[0] <= 0:
                self.x = 2

        def turn_left(self, evt):
            self.x = -4 #скорость движения налево

        def turn_right(self, evt):
            self.x = 4 #скорость движения направо






    class Ball: #мяч
        def __init__(self, canvas, bruh, hey, color):
            self.canvas = canvas
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color)#форма мяча
            self.canvas.move(self.id, 245, 300)#местопоявление
            self.bruh = bruh
            self.hey = hey
            starts = [-3, -2, -1, 1, 2, 3]#координаты полета
            start_ = [3,-3,2,-2]#еще координаты полета, тока другие
            random.shuffle(starts)
            random.shuffle(start_)
            self.x = starts[0]
            self.y = start_[0]
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.hit_bottom = False

        def hit_paddle(self, pos):#фиксатор столкновения по 1-платформе
            bruh_pos = self.canvas.coords(self.bruh.id)
            if pos[2] >= bruh_pos[0] and pos[0] <=  bruh_pos[2]:
                if pos[3] >= bruh_pos[1] and pos[3] <= bruh_pos[3]:
                    return True
            return False
        def hit_paddle_(self, pos):#фиксатор столкновения о 2-платформе
            hey_pos = self.canvas.coords(self.hey.id)
            if pos[2] >= hey_pos[0] and pos[0] <=  hey_pos[2]:
                if pos[3] >= hey_pos[1] and pos[3] <= hey_pos[3]:
                    return True
            return False

        def draw(self):#ключ программы
            self.canvas.move(self.id, self.x, self.y)#движение
            pos = self.canvas.coords(self.id)#координаты
            score_1 = Label(tk, text=str(str(o))).place(x=15, y=570)
            score_2 = Label(tk, text=str(str(o_))).place(x=15, y=15)
            if self.hit_paddle(pos) == True:#столкновение о 1-платформу
                self.y = -4
            if self.hit_paddle_(pos)==True:#столкновение о 2-платформу
                self.y = 4
            if pos[1] <= 0: #столкновение поверху
                game(o=o+1,o_=o_)


            if pos[3] >= self.canvas_height: #столкновение понизу
                game(o,o_=o_+1)





            elif pos[0] <= 0: #столкновение на лево
                self.x = 3

            elif pos[2] >= self.canvas_width: #столкновение на право
                self.x = -3
            if o == 10:
                g = messagebox.askokcancel('Game Over', 'Player 1 Won\nDo you want to continue?')
                if g==True:
                    game(0,0)
                elif g==False:
                    sys.exit()
            if o_==10:
                g = messagebox.askokcancel('Game Over', 'Player 1 Won\nDo you want to continue?')
                if g==True:
                    game(0,0)
                elif g==False:
                    sys.exit()




    tk.update()
    bruh = Bruh(canvas, 'gray')
    hey = Hey(canvas, 'gray')
    ball = Ball(canvas, bruh, hey, 'white')
    while 1: #запускает все программы и делает их бесконечными
        ball.draw()
        bruh.draw__()
        hey.draw_()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.008)
def game_():
    fin = PhotoImage(file="1560231201_2.png")
    canvas.create_image(200, 300, image=fin)
    class Bruh:#1-платформа
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(125,10,25,25,fill=color)#форма платфромы
            self.canvas.move(self.id, 200,500)#место появления платформы
            self.x = 0
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)#клавиша(налево)
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)#клавиша(направо)
        def draw__(self):#ключ
            self.canvas.move(self.id, self.x, 0)#движение
            pos = self.canvas.coords(self.id)#координаты

            if pos[0] <= 0: #ударение о правый край
                self.x = 2
            elif pos[2] >= self.canvas_width:
                self.x = -2

            if pos[2] >= self.canvas_width: #ударение о левый край
                self.x = -2
            elif pos[0] <= 0:
                self.x = 2

        def turn_left(self, evt):
                self.x = -4 #скорость движения налево
        def turn_right(self, evt):
                self.x = 4 #скорость движения направо

    class Ball:  # мяч
        def __init__(self, canvas, bruh, color):
            self.canvas = canvas
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # форма мяча
            self.canvas.move(self.id, 245, 300)  # местопоявление
            self.bruh = bruh
            starts = [-3, -2, -1, 1, 2, 3]  # координаты полета
            start_ = [3, -3, 2, -2]  # еще координаты полета, тока другие
            random.shuffle(starts)
            random.shuffle(start_)
            self.x = starts[0]
            self.y = start_[0]
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.hit_bottom = False

        def hit_paddle(self, pos):  # фиксатор удара по 1-платформе
            bruh_pos = self.canvas.coords(self.bruh.id)
            if pos[2] >= bruh_pos[0] and pos[0] <= bruh_pos[2]:
                if pos[3] >= bruh_pos[1] and pos[3] <= bruh_pos[3]:
                    return True
            return False

        def draw(self):  # ключ программы
            self.canvas.move(self.id, self.x, self.y)  # движение
            pos = self.canvas.coords(self.id)  # координаты
            if self.hit_paddle(pos) == True:  # столкновение о 1-платформу
                self.y = -4

            
                

            if pos[1] <= 0:  # столкновение поверху
                self.y = 3

            if pos[3] >= self.canvas_height:  # столкновение понизу
                #canvas.delete('all')  # стриает все
                game_()  # перезапускает игру





            elif pos[0] <= 0:  # столкновение на лево
                self.x = 3

            elif pos[2] >= self.canvas_width:  # столкновение на право
                self.x = -3

    tk.update()
    bruh = Bruh(canvas, 'gray')
    ball = Ball(canvas, bruh,'white')
    while 1:  # запускает все программы и делает их бесконечными
        ball.draw()
        bruh.draw__()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.008)

def two():
    b2.place_forget()
    b3.place_forget()
    game(0,0)
def one():
    b2.place_forget()
    b3.place_forget()
    game_()
b2 = Button(text = '1 PLAYER',font = 'Arial 10',bg = 'orange', fg = 'white', width=15, height = 3, command = one)
b3 = Button(text = '2 PLAYERS',font = 'Arial 10', bg = 'orange', fg = 'white',width=15, height = 3,command = two)

if now.hour > 5 and now.hour <= 12:
    morning = PhotoImage(file="evening_morning.png")
    canvas.create_image(50, 300, image=morning)
if now.hour >= 12 and now.hour <= 18:
    day = PhotoImage(file="day.png")
    canvas.create_image(50, 300, image=day)
if now.hour >=18 and now.hour <=22:
    morning = PhotoImage(file="evening_morning.png")
    canvas.create_image(50, 300, image=morning)
if now.hour >=22:
    night = PhotoImage(file="night.png")
    canvas.create_image(50, 300, image=night)

def ABC():
    b2.place(x = 145, y =230)
    b3.place(x = 145, y =290)
    b1.place_forget()

b1 = Button(text = 'PLAY',font = 'Arial 13',bg = 'orange', fg = 'yellow', bd = 3,width=15, height = 3, command = ABC)

b1.place(x = 130, y =250)
tk.mainloop()
