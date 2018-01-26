import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint



curses.initscr()
win = curses.newwin(20, 65, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)




key = KEY_RIGHT                                                    # First Values
score = 0

snake = [[4,10], [5,10], [6,10]]
food = [10,20]
bomb = [13,23]
bonus = [15,25]

win.addch(food[0], food[1], 'X')                                #prints food
win.addch(bomb[0], bomb[1], '*')                                #prints bombs

while key != 27:                                                   # While ESC not pressed
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.addstr(0, 27, ' Baltagih ')
    win.addstr(0,38,' Food X ')
    win.addstr(0,48,' Bomb * ')
    win.timeout(150 - (len(snake)/4 + len(snake)/8)%110)          # Speed increase with lenght

    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    key = key if event == -1 else event


    if key == ord(' '):                                           #SPACE to pause
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
        key = prevKey


        #increse lenght
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])


    # If you hit borders
    if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 64:
         break

    # If you eat yourself
    if snake[0] in snake[1:]:
        break


    if snake[0] == food:                                            # When food is eaten
        food = []
        score += 1
        if score%7 == 0:
            bonus = [randint(5, 15), randint(5, 10)]                # Next bonus coordinates
            win.addch(bonus[0],bonus[1], "B")
        if score%500 == 0:
            score += 150
        while food == []:
            food = [randint(1, 18), randint(1, 63)]                 # Next food coordinates
            bomb = [randint(5,15), randint(5,50)]                   # Next bomb coordinates
            if food in snake:
                 food = []
        win.addch(food[0], food[1], 'X')
        win.addch(bomb[0], bomb[1], '*')
        if snake[0] == bomb:
             break
    elif snake[0] == bonus:
        bonus = []
        score += 50
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], 'o')

curses.endwin()
print("\nScore - " + str(score))


