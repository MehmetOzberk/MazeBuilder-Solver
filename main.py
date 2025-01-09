from graphics import Window, Line, Point
def main():
    win = Window(800,600)
    # Create a Line object with the points
    line = Line(Point(50, 50), Point(300, 200))
    # Draw the line on the window's canvas
    win.draw_line(line, fill_color="black")
    win.wait_for_close()
    print("hello")

main()

