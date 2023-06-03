import colorgram
from turtle import Turtle, Screen
import random as rand

# colors = colorgram.extract('image.jpg', 20)

# print(colors[0].rgb)

# first_color = colors[0]
# rgb = first_color.rgb
# red = rgb[0]
# print(red)

# colors_list = []

# colors_list.append(first_color.rgb[0])
# colors_list.append(first_color.rgb[1])
# colors_list.append(first_color.rgb[2])

# print(colors_list)

# for index, color in enumerate(colors):
#     color_selection = colors[index]
#     rgb = color_selection.rgb
#     for color in rgb:
#         colors_list.append(color)

# print(colors_list)

# for color in colors:
#     rgb = color.rgb
#     colors_list.append(tuple(rgb))

# rgb_colors = [tuple(color.rgb) for color in colors]

# print(rgb_colors)

color_list = [(233, 239, 246), (246, 239, 242), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]

# 100 dots in total
# 10x10
# Dot size 20
# Spaced by 50 paces

pen = Turtle()
pen.shape('classic')
pen.pensize(20)
pen.speed(0)

screen = Screen()
screen.colormode(255)

def painting():
    posx = -230
    posy = -200
    for _ in range(10):
        pen.penup()
        pen.setposition(posx, posy)
        
        for _ in range(10):
            pen.color(rand.choice(color_list))
            pen.dot(20)
            pen.penup()
            pen.forward(50)
            posy += 5

painting()

screen.exitonclick()