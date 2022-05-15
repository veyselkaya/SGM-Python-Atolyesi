import turtle as t


t.speed(20)
renkler = ["red", "blue", "yellow", "indigo"]
for i in range(20):
    t.color(renkler[i%4])
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.circle(20)

    t.color(renkler[i % 4])
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.circle(20)

    t.color(renkler[i % 4])
    t.penup()
    t.goto(100, 0)
    t.pendown()
    t.circle(20)

    t.color(renkler[i % 4])
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.circle(20)

    t.left(18)

t.mainloop()