import turtle as t
import random as r

t.speed(20)
renkler = ["red", "blue", "green", "lime", "yellow", "indigo"]

for i in range(50):
    t.begin_fill()
    t.color(renkler[i%6])
    for i in range(5):
        t.forward(50)
        t.left(144)
    t.end_fill()

    t.penup()
    t.goto(r.randint(-300, 300), r.randint(-300, 300))
    t.pendown()

    t.circle(i*5)

    for i in range(4):
        t.forward(90)
        t.left(90)













t.mainloop()