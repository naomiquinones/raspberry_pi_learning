from sense_hat import SenseHat

sh = SenseHat()

gold = (225, 180, 0)
purple = (50, 0, 70)

sh.show_message("Hi!", text_colour=gold, back_colour=purple, scroll_speed=.75)


sh.clear()
