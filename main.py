from graphics import *

def main():
    win = Window(800, 600)
    point1 = Point(100, 200)
    point2 = Point(200, 500)
    point3 = Point(600, 300)
    point4 = Point(500, 500)
    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point1)
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "blue")
    win.draw_line(line4, "black")
    win.wait_for_close()

main()