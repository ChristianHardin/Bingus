import curses
from curses import wrapper

def main(stdscreen):
    height, width = stdscreen.getmaxyx()
    stdscreen.clear()
    stdscreen.refresh()

    pad = curses.newpad(5, width-10)
    for y in range(0, 5):
        for x in range(0, width-11):
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

    pad.refresh(0,0, int((height/2)-3),5, int((height/2)+2),width-10)
    stdscreen.getkey() 

wrapper(main)
