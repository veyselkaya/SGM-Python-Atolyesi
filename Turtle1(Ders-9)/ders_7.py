import turtle as t


t.speed(20)

for i in range(20):
    t.color("blue")
    t.bgcolor("red")
    for i in range(20):
        t.circle(100)
        t.left(18)

    t.color("red")
    t.bgcolor("blue")
    for i in range(20):
        t.circle(100)
        t.left(18)


t.mainloop()