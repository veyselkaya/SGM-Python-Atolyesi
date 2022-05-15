import turtle as t




t.speed(20)
renkler = ["red", "blue", "yellow", "indigo"]
for i in range(20):
    t.color(renkler[i%4])
    t.circle(i*10)

t.left(180)

for i in range(20):
    t.color(renkler[i % 4])
    t.circle(i*10)

t.mainloop()