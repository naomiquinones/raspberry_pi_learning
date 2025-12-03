from sense_hat import SenseHat

sh = SenseHat()

red = (205, 0, 0)
green = (0, 180, 0)
blue = (0, 0, 230)
magenta = (240, 0, 255)
white = (255, 255, 255)
yellow = (225, 195, 0)

sh.clear()
sh.set_pixel(2, 2, green)
sh.set_pixel(5, 2, green)
sh.set_pixel(3, 4, magenta)
sh.set_pixel(4, 4, magenta)
sh.set_pixel(1, 5, red)
sh.set_pixel(2, 6, red)
sh.set_pixel(3, 6, red)
sh.set_pixel(4, 6, red)
sh.set_pixel(5, 6, red)
sh.set_pixel(6, 5, red)

