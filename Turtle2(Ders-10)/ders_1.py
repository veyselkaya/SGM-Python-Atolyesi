import turtle as t


def kare(kenar, x,y):
    t.speed(20)
    for i in range(4):
        t.forward(kenar)
        t.left(90)
    t.penup()
    t.goto(x,y)
    t.pendown()

def cember(yaricap, x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(yaricap)

# kare(100,100,100)
# kare(200, -100,100)
# kare(100,100,-100)
# cember(30, -20, 90)


for i in range(10):
     kare(50, 20,20)
     t.left(36)


t.color("lime")
for i in range(10):
    cember(50, 100,100)
    t.left(36)



t.mainloop()