import curses


def char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        ch = win.getch()
    finally:
        curses.endwin()
    return chr(ch)