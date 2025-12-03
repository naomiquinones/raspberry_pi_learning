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

sh.clear()

grid = [
    b, b, b, b, b, b, b, b,
    b, c, c, c, c, c, c, b,
    c, c, c, g, g, c, c, c,
    c, g, g, y, y, g, g, c,
    g, y, y, o, o, y, y, g,
    y, o, o, r, r, o, o, y,
    o, r, r, w, w, r, r, o,
    r, w, w, w, w, w, w, r
]
sh.set_pixels(grid)

