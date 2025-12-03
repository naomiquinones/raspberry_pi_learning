from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

red = (205, 0, 0)
green = (0, 180, 0)
blue = (0, 0, 230)
magenta = (240, 0, 255)
white = (255, 255, 255)
yellow = (225, 195, 0)

sh.show_letter("N", red)
sleep(1)
sh.show_letter("a", magenta)
sleep(1)
sh.show_letter("o", blue)
sleep(1)
sh.show_letter("m", green)
sleep(1)
sh.show_letter("i", yellow)
sleep(1)

sh.clear()
