import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
wn.title("Equilateral Triangle")
wn.bgcolor("orange")
tess.color("yellow")
tess.pensize(9)
for i in[0,1,2]:
    tess.forward(50)
    tess.left(120)
wn.mainloop()
