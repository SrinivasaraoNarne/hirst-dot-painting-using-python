# import colorgram
#
# colors = colorgram.extract('image.jpg', 25)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")

paint_colors = [(184, 147, 94), (151, 104, 46), (178, 150, 22), (83, 34, 27), (12, 57, 73), (31, 100, 120),
                (101, 41, 47), (56, 137, 122), (108, 39, 29), (22, 65, 50), (39, 81, 7), (94, 62, 68), (199, 91, 65),
                (110, 8, 9), (116, 167, 77), (131, 178, 92), (139, 167, 176), (217, 203, 140), (179, 148, 151),
                (177, 205, 178), (226, 177, 167)]

tim.penup()
tim.setheading(225)
tim.forward(250)
tim.pendown()
tim.setheading(0)

i = 0
while i < 10:
    for _ in range(10):
        tim.dot(20, random.choice(paint_colors))
        tim.penup()
        tim.forward(40)
        tim.pendown()

    tim.penup()
    tim.setheading(90)
    tim.forward(40)
    tim.setheading(180)
    tim.forward(400)
    tim.setheading(0)
    tim.pendown()

    i += 1

my_screen = turtle.Screen()
my_screen.exitonclick()
