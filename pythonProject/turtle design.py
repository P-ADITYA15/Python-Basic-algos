from turtle import*
t = Turtle()
s = Screen()
t.speed(99)
t.shape("turtle")
s.bgcolor("light blue")
t.color("red","black")
def adi():

    for i in range(100):
        t.forward(100)
        t.right(76)
        if i%4==0:
            t.forward(50)

t.fillcolor("orange")
t.begin_fill()
adi()
t.end_fill()
t.forward(200)
t.fillcolor("green")
t.begin_fill()

adi()
t.end_fill()
t.forward(-180)
t.fillcolor("white")
t.begin_fill()
adi()
t.end_fill()

done()