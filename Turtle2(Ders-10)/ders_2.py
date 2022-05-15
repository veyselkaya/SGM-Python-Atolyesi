import random
import turtle as t
import random as r

def cember(yaricap):
    t.speed(20)
    t.circle(yaricap)

renk = ["red", "blue", "green", "lime", "yellow"]

for i in range(30):
    for i in range(6):
        t.color(renk[r.randint(0, 4)])
        cember(i * 10)

    t.left(-90)

    for i in range(6):
        t.color(renk[r.randint(0, 4)])
        cember(i * 10)
t.left(90)




t.mainloop()