import turtle

Screen = turtle.Turtle()
color= ['red','green','blue','yellow','purple']
wn =turtle.Screen()
wn.bgcolor("black")
turtle.pensize(4)
turtle.penup()
turtle.setpos(-90,30)
turtle.pendown()
for i in range(5):
    turtle.pencolor(color[i])
    turtle.forward(200)
    turtle.right(144)
 
turtle.penup()
turtle.setpos(80,-140)
turtle.pendown()
turtle.pencolor("Black")
turtle.done()