import colorgram

colors = colorgram.extract('image.jpg', 12)

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

colors_list = [tuple(color.rgb) for color in colors]

# print(colors_list)