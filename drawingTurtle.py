import turtle

def draw_square():
    
    window = turtle.Screen()
    window.bgcolor = ("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(100)

    i = 0
    brad.left(r)
    while (i<4):
        brad.forward(100)
        brad.right(90)
        i = i + 1

    brad.left(r)
    
    #window.exitonclick()

def draw_circle():
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(25)

    angie.circle(10)


def draw_triangle():

    trio = turtle.Turtle()
    trio.shape("turtle")
    trio.color("blue")
    trio.speed(2)

    trio.left(r)
    for x in range (3):
        trio.left(120)
        trio.forward(150)

    trio.left(r)

r = 0;
while (r < 360):
    draw_square()
    r = r + 5

    
#draw_triangle()
#draw_circle()



