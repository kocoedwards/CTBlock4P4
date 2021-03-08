import turtle

print("What shape would you like to draw? Square or Triangle")
player = input(">")

if plyer.lower() == "square":
    window = turtle.Screen()
    cube = turtle.Turtle()
for x in range (0, 4):
    cube.forward(100)
    cube.left(90)
elif player.lower() == "triangle":
    window = turtle.Screen()
    cube = turtle.Turtle()
for x in range (0, 3):
    cube.forward(100)
    cube.left(120)
else:
    print("Square or Triangle, please!")
