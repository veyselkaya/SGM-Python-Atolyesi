import turtle as t


t.speed(20)
renkler = ["red", "blue", "green", "lime", "yellow", "indigo"]

t.bgcolor("black")


for i in range(360):
    t.pencolor(renkler[i%6])
    t.width(10-i*0.025)
    t.forward(i)
    t.left(59)

t.mainloop()