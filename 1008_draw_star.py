import turtle
turtle.Screen().bgcolor('cornflowerblue')

turtle.Screen().setup(600,500)

p = turtle.Turtle()
p.color('red')
p.pensize(5)
p.shape('turtle')

p.penup()
p.goto(0, 100)
p.pendown()

for _ in range(5):
    p.forward(200)
    p.right(144) 
        
turtle.done()

