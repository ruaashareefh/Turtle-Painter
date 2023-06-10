import turtle as t
import random

tim = t.Turtle()
tim.speed(0)

color_list = [(220, 159, 84), (39, 109, 150), (119, 163, 191), (150, 63, 87),
              (217, 232, 222), (203, 134, 157), (180, 159, 35), (32, 131, 95), (122, 179, 151),
              (235, 217, 224), (161, 80, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231),
              (229, 199, 114), (140, 32, 42), (56, 166, 135), (8, 105, 80), (47, 158, 182),
              (234, 163, 181), (117, 114, 162), (32, 62, 111), (236, 171, 157), (125, 38, 35),
              (156, 210, 196), (32, 57, 79), (70, 41, 37), (25, 65, 55), (73, 37, 47)]

t.colormode(255)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()

screen = t.Screen()
screen.exitonclick()

