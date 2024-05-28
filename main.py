import curses
from curses import wrapper

def main(stdscreen):
    stdscreen.clear()
    stdscreen.addstr('test')
    stdscreen.refresh()
    stdscreen.getkey()


wrapper(main)
