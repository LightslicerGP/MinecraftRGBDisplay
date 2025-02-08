from PIL import Image

original = Image.open("Images/color_wheel.png").convert("RGB")
color_states = 4
width, height = original.size

new_typeA = Image.new("RGB", (width, height))
new_typeB = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        r, g, b = original.getpixel((x, y))

        Ar, Ag, Ab = (int(255/color_states)*int(color_states*(x/255)) for x in (r, g, b))

        Br, Bg, Bb = (
            int(((x * color_states) // 256) * (255 / (color_states - 1))) for x in (r, g, b)
        )

        new_typeA.putpixel((x, y), (Ar, Ag, Ab))
        new_typeB.putpixel((x, y), (Br, Bg, Bb))

new_typeA.save("converted_quantized.png")
new_typeB.save("converted_quantizedGPT.png")
