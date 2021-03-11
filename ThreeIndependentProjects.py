import turtle

print("What shape do you want to create? A Hexagon or Star?")
player = input(">")

if player.lower() == "hexagon":
    window = turtle.Screen()
    cube = turtle.Turtle()
    s = int(input("90"))
    col = input("blue")
    t.fillcolor(col)
    t.begin_fill()
    for x in range (0, 6):
         cube.forward(90)
         cube.left(300)
    t.end_fill()


elif player.lower() == "star":
    window = turtle.Screen()
    cube = turtle.Turtle()
    s = int(input("100"))
    col = input("red")
    t.fillcolor(col)
    t.begin_fill()
    for x in range (0, 10):
       cube.forward(100)
       cube.right(144)
    t.end_fill()
       
