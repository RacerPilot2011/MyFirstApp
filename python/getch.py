import curses


def char(message):
    try:
        win = curses.initscr()
        n = curses.newwin()
        win.addstr(0, 0, message)
        n.nodelay(True)
        ch = win.getch()
    finally:
        curses.endwin()
    return chr(ch)