import turtle as t


t.speed(20)
renkler = ["red", "yellow", "blue", "green", "black", "pink", "lime"]
for i in range(36):
    t.color(renkler[i%7])
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.left(10)






t.mainloop()