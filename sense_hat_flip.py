from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

r = (205, 0, 0)
g = (0, 180, 0)
b = (0, 0, 230)
c = (0, 180, 230)
m = (240, 0, 255)
w = (150, 150, 150)
y = (225, 195, 0)
o = (230, 180, 0)
p = (50, 0, 50)
k = (0, 0, 0)

sh.clear()

grid = [
    p, p, m, w, r, o, o, y,
    p, p, m, m, w, r, o, o,
    p, o, c, c, c, k, r, o,
    c, o, c, c, c, c, k, r,
    w, w, o, c, c, b, b, k,
    w, r, o, b, b, c, g, g,
    w, r, o, c, c, b, g, k,
    w, r, r, b, b, b, g, g
]
sh.set_pixels(grid)

while True:
    sleep(3)
    sh.flip_h()
