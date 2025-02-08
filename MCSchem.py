import mcschematic
from PIL import Image

og_image = Image.open("Images/TrueTest48x27.png")
if og_image.mode == "RGBA":
    og_image = og_image.convert("RGB")
og_width, og_height = og_image.size

schem = mcschematic.MCSchematic()


for y in range(og_height):
    for x in range(og_width):
        og_color = og_image.getpixel((x, y))
        r, g, b = og_color 

        r, g, b = ((x * 4) // 256 for x in (r, g, b))
        new_color = (r, g, b)
        new_x = x * -7
        new_y = y * -7

        if r == 0:
            schem.setBlock((new_x - 1, new_y - 2, 0), "minecraft:air")
            schem.setBlock((new_x - 1, new_y - 4, 0), "minecraft:air")
        elif r == 1:
            schem.setBlock((new_x - 1, new_y - 2, 0), "minecraft:air")
            schem.setBlock((new_x - 1, new_y - 4, 0), "minecraft:redstone_block")
        elif r == 2:
            schem.setBlock((new_x - 1, new_y - 2, 0), "minecraft:redstone_block")
            schem.setBlock((new_x - 1, new_y - 4, 0), "minecraft:air")
        elif r == 3:
            schem.setBlock((new_x - 1, new_y - 4, 0), "minecraft:redstone_block")
            schem.setBlock((new_x - 1, new_y - 2, 0), "minecraft:redstone_block")

        if g == 0:
            schem.setBlock((new_x - 3, new_y - 2, 0), "minecraft:air")
            schem.setBlock((new_x - 3, new_y - 4, 0), "minecraft:air")
        elif g == 1:
            schem.setBlock((new_x - 3, new_y - 2, 0), "minecraft:air")
            schem.setBlock((new_x - 3, new_y - 4, 0), "minecraft:redstone_block")
        elif g == 2:
            schem.setBlock((new_x - 3, new_y - 2, 0), "minecraft:redstone_block")
            schem.setBlock((new_x - 3, new_y - 4, 0), "minecraft:air")
        elif g == 3:
            schem.setBlock((new_x - 3, new_y - 4, 0), "minecraft:redstone_block")
            schem.setBlock((new_x - 3, new_y - 2, 0), "minecraft:redstone_block")

        if b == 0:
            schem.setBlock((new_x - 5, new_y - 2, 0), "minecraft:air")
            schem.setBlock((new_x - 5, new_y - 4, 0), "minecraft:air")
        elif b == 1:
            schem.setBlock((new_x - 5, new_y - 2, 0), "minecraft:air")
            schem.setBlock((new_x - 5, new_y - 4, 0), "minecraft:redstone_block")
        elif b == 2:
            schem.setBlock((new_x - 5, new_y - 2, 0), "minecraft:redstone_block")
            schem.setBlock((new_x - 5, new_y - 4, 0), "minecraft:air")
        elif b == 3:
            schem.setBlock((new_x - 5, new_y - 4, 0), "minecraft:redstone_block")
            schem.setBlock((new_x - 5, new_y - 2, 0), "minecraft:redstone_block")

og_image.close()

schem.save(
    "C:/Users/LightslicerGP/AppData/Roaming/.minecraft/installations/Iris 1.18.2/config/worldedit/schematics",
    "display_blocks",
    mcschematic.Version.JE_1_18_2,
)
