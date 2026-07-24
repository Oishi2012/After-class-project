import turtle

turtle.Screen().bgcolor("Blue")

mypen=turtle.Turtle()

#Triangle
mypen.penup()
mypen.goto(-150,0)
mypen.pendown()

mypen.forward(100)
mypen.left(120)
mypen.forward(100)
mypen.left(120)
mypen.forward(100)


#Rectangle
mypen.penup()
mypen.goto(50,0)
mypen.pendown()

mypen.forward(150)
mypen.left(90)
mypen.forward(100)
mypen.left(90)
mypen.forward(150)
mypen.left(90)
mypen.forward(100)

turtle.done()