from PIL import Image

height = 128
width = 255 * 6
image = Image.new("RGB", (width, height))

r, g, b = 255, 0, 0

for x in range(width):
    for y in range(height):
        image.putpixel((x, y), (r, g, b))
    
    if 0 <= x < 255:
        g += 1
    elif 255 <= x < 255 * 2:
        r -= 1
    elif 255 * 2 <= x < 255 * 3:
        b += 1
    elif 255 * 3 <= x < 255 * 4:
        g -= 1
    elif 255 * 4 <= x < 255 * 5:
        r += 1
    else:
        b -= 1

image.save("color_wheel.png")


''' 3/7/24 - my own version, compared to chatgpt's optimized one
from PIL import Image

height = 128
width = (255 * 6)

r = 255
g = 0
b = 0
x = -1

image = Image.new("RGB", (width, height))

while x <= width:
    while 254 >= g:
        g += 1
        x += 1
        for y in range(height):
            rgb_color = (r, g, b)
            image.putpixel((x, y), rgb_color)
    while 1 <= r:
        r -= 1
        x += 1
        for y in range(height):
            rgb_color = (r, g, b)
            image.putpixel((x, y), rgb_color)
    while 254 >= b:
        b += 1
        x += 1
        for y in range(height):
            rgb_color = (r, g, b)
            image.putpixel((x, y), rgb_color)
    while 1 <= g:
        g -= 1
        x += 1
        for y in range(height):
            rgb_color = (r, g, b)
            image.putpixel((x, y), rgb_color)
    while 254 >= r:
        r += 1
        x += 1
        for y in range(height):
            rgb_color = (r, g, b)
            image.putpixel((x, y), rgb_color)
    while 1 <= b:
        b -= 1
        x += 1
        for y in range(height):
            rgb_color = (r, g, b)
            image.putpixel((x, y), rgb_color)
    break


image.save("Images\color_wheel.png")
'''