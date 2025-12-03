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

bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_bat():
    sh.set_pixel(0, bat_y, p)
    sh.set_pixel(0, bat_y + 1, p)
    sh.set_pixel(0, bat_y - 1, p)

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1

def draw_ball():
    sh.set_pixel(ball_position[0], ball_position[1], w)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y + 1):
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 0:
        sh.show_message("You lose")

while True:
    sh.clear(k)
    sh.stick.direction_up = move_up
    sh.stick.direction_down = move_down
    draw_bat()
    draw_ball()
    sleep(.25)

sleep(1)
sh.clear()

