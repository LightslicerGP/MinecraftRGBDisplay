# MADE by LightslicerGP, completed 3/7/24, might make a better version of this idk - 3/7/24
# MADE by LightslicerGP, 6x6 part made to fit the new display prototype 6/17/24

from PIL import Image

og_image = Image.open("Images/grass.png")

if og_image.mode == "RGBA":
    og_image = og_image.convert("RGB")

og_width, og_height = og_image.size


def gensim():

    simulated_image = Image.new("RGB", (og_width, og_height))

    for y in range(og_height):
        for x in range(og_width):
            og_color = og_image.getpixel((x, y))
            r, g, b = og_color

            simr, simg, simb = (((x * 4) // 256) * 85 for x in (r, g, b))
            sim_color = (simr, simg, simb)

            simulated_image.putpixel((x, y), sim_color)

    simulated_image.save("simulated_image.png")


def gen3x3():

    new_width = (og_width * 4) + 1
    new_height = (og_height * 4) + 1
    new_image = Image.new("RGB", (new_width, new_height))

    for y in range(og_height):
        for x in range(og_width):
            og_color = og_image.getpixel((x, y))
            r, g, b = og_color

            r, g, b = ((x * 4) // 256 for x in (r, g, b))
            # new_color = (r, g, b)

            new_x = x * 4
            new_y = y * 4

            if r == 1:
                new_image.putpixel((new_x + 1, new_y + 2), (255, 0, 0))
            elif r == 2:
                new_image.putpixel((new_x + 1, new_y + 1), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 3), (255, 0, 0))
            elif r == 3:
                new_image.putpixel((new_x + 1, new_y + 1), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 2), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 3), (255, 0, 0))

            if g == 1:
                new_image.putpixel((new_x + 2, new_y + 2), (0, 255, 0))
            elif g == 2:
                new_image.putpixel((new_x + 2, new_y + 1), (0, 255, 0))
                new_image.putpixel((new_x + 2, new_y + 3), (0, 255, 0))
            elif g == 3:
                new_image.putpixel((new_x + 2, new_y + 1), (0, 255, 0))
                new_image.putpixel((new_x + 2, new_y + 2), (0, 255, 0))
                new_image.putpixel((new_x + 2, new_y + 3), (0, 255, 0))

            if b == 1:
                new_image.putpixel((new_x + 3, new_y + 2), (0, 0, 255))
            elif b == 2:
                new_image.putpixel((new_x + 3, new_y + 1), (0, 0, 255))
                new_image.putpixel((new_x + 3, new_y + 3), (0, 0, 255))
            elif b == 3:
                new_image.putpixel((new_x + 3, new_y + 1), (0, 0, 255))
                new_image.putpixel((new_x + 3, new_y + 2), (0, 0, 255))
                new_image.putpixel((new_x + 3, new_y + 3), (0, 0, 255))

    new_image.save("final_image_3x3.png")


def gen6x6():

    new_width = (og_width * 7) + 1
    new_height = (og_height * 7) + 1

    new_image = Image.new("RGB", (new_width, new_height))

    for y in range(og_height):
        for x in range(og_width):
            og_color = og_image.getpixel((x, y))
            r, g, b = og_color

            r, g, b = ((x * 4) // 256 for x in (r, g, b))

            new_x = x * 7
            new_y = y * 7

            if r == 1:
                new_image.putpixel((new_x + 1, new_y + 3), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 4), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 3), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 4), (255, 0, 0))
            elif r == 2:
                new_image.putpixel((new_x + 1, new_y + 1), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 2), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 1), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 2), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 5), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 6), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 5), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 6), (255, 0, 0))
            elif r == 3:
                new_image.putpixel((new_x + 1, new_y + 3), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 4), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 3), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 4), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 1), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 2), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 1), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 2), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 5), (255, 0, 0))
                new_image.putpixel((new_x + 1, new_y + 6), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 5), (255, 0, 0))
                new_image.putpixel((new_x + 2, new_y + 6), (255, 0, 0))

            if g == 1:
                new_image.putpixel((new_x + 3, new_y + 3), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 4), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 3), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 4), (0, 255, 0))
            elif g == 2:
                new_image.putpixel((new_x + 3, new_y + 1), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 2), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 1), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 2), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 5), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 6), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 5), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 6), (0, 255, 0))
            elif g == 3:
                new_image.putpixel((new_x + 3, new_y + 3), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 4), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 3), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 4), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 1), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 2), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 1), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 2), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 5), (0, 255, 0))
                new_image.putpixel((new_x + 3, new_y + 6), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 5), (0, 255, 0))
                new_image.putpixel((new_x + 4, new_y + 6), (0, 255, 0))

            if b == 1:
                new_image.putpixel((new_x + 5, new_y + 3), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 4), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 3), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 4), (0, 0, 255))
            elif b == 2:
                new_image.putpixel((new_x + 5, new_y + 1), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 2), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 1), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 2), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 5), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 6), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 5), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 6), (0, 0, 255))
            elif b == 3:
                new_image.putpixel((new_x + 5, new_y + 3), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 4), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 3), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 4), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 1), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 2), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 1), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 2), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 5), (0, 0, 255))
                new_image.putpixel((new_x + 5, new_y + 6), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 5), (0, 0, 255))
                new_image.putpixel((new_x + 6, new_y + 6), (0, 0, 255))

    new_image.save("final_image_6x6.png")

gensim()
gen3x3()
gen6x6()
og_image.close()

# none = 0
# one = 0
# two = 0
# three = 0

# for i in range(0, 256):
#     print(i)
#     num = (i * 4) // 256
#     print(num)
#     if num == 0:
#         none += 1
#     elif num == 1:
#         one += 1
#     elif num == 2:
#         two += 1
#     elif num == 3:
#         three += 1

# print(none, one, two, three)
