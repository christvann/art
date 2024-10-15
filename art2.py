import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
color = ('green', 'blue', 'yellow', 'red', 'white', 'aqua')
for i in range(320):
    t.color(color[i%6])
    t.left(154)
    t.forward(i*2)