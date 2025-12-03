from sense_hat import SenseHat

sh = SenseHat()

r = (205, 0, 0)
g = (0, 180, 0)
b = (0, 0, 230)
c = (0, 180, 230)
m = (240, 0, 255)
w = (255, 255, 255)
y = (225, 195, 0)
o = (230, 180, 0)
p = (50, 0, 50)

sh.clear()

minecraft_grid = [
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, c, c, c, c, c, c, p,
    c, c, c, c, c, c, c, c,
    c, w, b, c, c, b, w, c,
    c, c, c, b, b, c, c, c,
    c, c, b, c, c, b, c, c,
    c, c, b, b, b, b, c, c
]
sh.set_pixels(minecraft_grid)

