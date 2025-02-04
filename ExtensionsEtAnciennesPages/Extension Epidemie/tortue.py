from turtle import *
colore=["red", "green", "blue"]*10
speed(100)
for j in range(4):
    for i in range(10,100,10):
        color(colore[(i-10)//10])
        circle(i)
    right(90)
done()