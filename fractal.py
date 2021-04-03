from math import *
import turtle as tur
tu = tur.Turtle()
wn = tur.Screen()


def draw_line(size, n):
    dd = 180-degrees(atan(0.47/0.03)) # here you can put the angle you need (using degrees) instead of degrees(atan(0.47/0.03))
    if n == 0:
        tu.color('red')
        tu.forward(size*0.47/cos(dd))
    else:
        next_size = size * 0.47
        next_n = n - 1
        draw_line(next_size, next_n)
        tu.right(180-dd)
        draw_line(next_size, next_n)
        tu.left((180-dd) * 2)
        draw_line(next_size, next_n)
        tu.right(180-dd)
        draw_line(next_size, next_n)


def torn_square(size, n):
    for i in range(4):
        draw_line(size, n)
        tu.right(90)


if __name__ == '__main__':
    tu.screen.bgcolor('black')
    tu.speed(1000)
    tu.pu()

    tu.setposition(-170, 200)
    tu.pd()
    torn_square(200, 2)
    wn.exitonclick()
