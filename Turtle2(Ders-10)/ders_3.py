import turtle as t


t.speed(20)
t.bgcolor("cyan")

renkler = ["red", "blue", "green", "lime", "yellow", "indigo"]

for i in range(36):
    t.color(renkler[i%6])
    t.circle(i*5)
    t.circle(-i*5)
    t.left(i)



#ödev yukarıda buluna  şeklin ters çalışan halini yapınız
for i in range(36):
    t.color(renkler[i%6])
    t.circle(-i*5)
    t.circle(i*5)
    t.left(i)



t.mainloop()