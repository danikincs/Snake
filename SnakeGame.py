import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import sys
import time
import random
from random import randint
curses.initscr()
curses.start_color()
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Initializing colors
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)


def add():                                    # Add .txt file if not exists, stores player score.
    input_file = open("name.txt", "a")
    name = input("enter your username: ")
    print(name, " ", score, file=input_file)
    input_file.close()


def print_score():                           # Shows scores in terminal, previous scores also appears
    output_file = open("name.txt", "r+")
    text_in_file = output_file.read()
    print(text_in_file)
    output_file.close()
    exit()


def multiplayer_ready_screen(scr):  # Multiplayer start screen, contains information
    player_1_ready = False
    player_2_ready = False
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win.clear()
    win.nodelay(0)
    message1 = "Welcome to the Multiplayer Fight !"
    message2 = "Player 1 press 'ENTER' to Ready!"
    message3 = "Player 1 movement: arrows | Player 2 movement: WASD"
    win.addstr((curses.LINES) // 2, (curses.COLS - len(message1)) // 2, message1)
    win.addstr(((curses.LINES) // 2)+2, ((curses.COLS - len(message2)) // 2), message2, curses.color_pair(2))
    win.addstr(((curses.LINES) // 2)+1, ((curses.COLS - len(message3)) // 2), message3)
    event2 = win.getch()
    if event2 == ord("\n"):
        player_2_ready = True
        message4 = "Player 2 press 'W' to Ready!"
        win.addstr(((curses.LINES) // 2)+3, ((curses.COLS - len(message4)) // 2), message4, curses.color_pair(1))
        win.refresh()
    event = win.getch()
    if event == ord("w"):
        player_1_ready = True
        win.refresh
        time.sleep(0.5)

    if player_1_ready is True and player_2_ready is True:
        multi_player(scr)


def start_screen(scr):      # Start menu where you can choose single, or multiplayer game mode.
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win.clear()
    win.nodelay(0)
    message1 = "Welcome to the Sneaky Game !"
    message2 = "Press 1 to Single Player | Press 2 to Multi Player!"
    win.addstr((curses.LINES) // 2, (curses.COLS - len(message1)) // 2, message1)
    win.addstr(((curses.LINES) // 2)+2, ((curses.COLS - len(message2)) // 2)+2, message2)
    event = win.getch()
    if event == ord("1"):
        single_player(scr)
    if event == ord("2"):
        multiplayer_ready_screen(scr)


def end_scene(scr):   # It appears, when player loses, replays or quits (single player)
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win.clear()
    win.nodelay(0)
    message3 = "Your score is : " + str(score)
    message1 = "Game Over!"
    message2 = "Press Q to quit, or Press P to Play Again!"
    win.addstr((curses.LINES) // 2, (curses.COLS - len(message1)) // 2, message1)
    win.addstr(((curses.LINES) // 2)+2, ((curses.COLS - len(message2)) // 2)+2, message2)
    win.addstr(((curses.LINES) // 2)-2, ((curses.COLS - len(message3)) // 2), message3)
    event = win.getch()
    if event == ord("p"):
        start_screen(scr)
    if event == ord("q"):
        curses.endwin()
        add()
        print_score()
    else:
        exit()
    time.sleep(1)


def multi_player_end_scene(scr):  # Same as above just in Multiplayer
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win.clear()
    curses.endwin()
    win.nodelay(0)
    global winner
    if score_1 > score_2:  # Player 1 winning
        message1 = "Player 1 has won!"
        message2 = "Player 1 score : " + str(score_1)
        message3 = "Game is over!"
        message4 = "Press Q to quit, or Press P to Play Again!"
        win.addstr(curses.LINES // 2, (curses.COLS - len(message1)) // 2, message1)
        win.addstr(curses.LINES // 2+2, (curses.COLS - len(message2)) // 2, message2)
        win.addstr(curses.LINES // 2-2, (curses.COLS - len(message3)) // 2, message3)
        win.addstr(curses.LINES // 2+4, (curses.COLS - len(message4)) // 2, message4)
        event = win.getch()
        if event == ord("p"):
            start_screen(scr)
        if event == ord("q"):
            curses.endwin()
            time.sleep(1)
            exit()
        else:
            exit()
    if score_2 > score_1:  # Player 2 winning
        message1 = "Player 2 has won!"
        message2 = "Player 2 score : " + str(score_2)
        message3 = "Game is over!"
        message4 = "Press Q to quit, or Press P to Play Again!"
        win.addstr(curses.LINES // 2, (curses.COLS - len(message1)) // 2, message1)
        win.addstr(curses.LINES // 2+2, (curses.COLS - len(message2)) // 2, message2)
        win.addstr(curses.LINES // 2-2, (curses.COLS - len(message3)) // 2, message3)
        win.addstr(curses.LINES // 2+4, (curses.COLS - len(message4)) // 2, message4)
        event = win.getch()
        if event == ord("p"):
            start_screen(scr)
        if event == ord("q"):
            curses.endwin()
            time.sleep(1)
            exit()
        else:
            exit()
    if score_2 == score_1:  # If score equals
        message1 = "Nobody Won"
        message3 = "Game is over!"
        message4 = "Press Q to quit, or Press P to Play Again!"
        win.addstr(curses.LINES // 2, (curses.COLS - len(message1)) // 2, message1)
        win.addstr(curses.LINES // 2-2, (curses.COLS - len(message3)) // 2, message3)
        win.addstr(curses.LINES // 2+4, (curses.COLS - len(message4)) // 2, message4)
        event = win.getch()
        if event == ord("p"):
            start_screen(scr)
        if event == ord("q"):
            curses.endwin()
            time.sleep(1)
            exit()


def single_player(scr):  # Main single player running
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    min_max = [curses.LINES, curses.COLS]
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    game_over = False
    curses.start_color()

    key = KEY_RIGHT
    global score                                                       # Initializing values
    score = 0

    snake = [[4, 10], [4, 9], [4, 8]]                                  # Initial snake co-ordinates
    food = [10, 20]                                                    # First food co-ordinates
    snake = [[4, 10], [4, 9], [4, 8]]                                  # Initial snake co-ordinates
    food = [10, 20]                                                    # First food co-ordinates
    enemy = [20, 10]
    win.addch(enemy[0], enemy[1], '-')
    win.addch(food[0], food[1], '*')                                   # Printing the food

    while key != 27 or game_over is False:                             # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        win.addstr(0, 27, ' SNAKE ')
        win.timeout(90 - (len(snake) + 1))

        prevKey = key                                                  # Previous key pressed
        event = win.getch()

        if event != -1:
            key = event

        if key == ord(' '):
            key = -1                                                   # (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey
        if prevKey == KEY_UP:
            if key in [KEY_DOWN]:
                key = prevKey
        if prevKey == KEY_DOWN:
            if key in [KEY_UP]:
                key = prevKey
        if prevKey == KEY_RIGHT:
            if key in [KEY_LEFT]:
                key = prevKey
        if prevKey == KEY_LEFT:
            if key in [KEY_RIGHT]:
                key = prevKey

        snake.insert(
            0,
            [
                snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),  # Snake movement
                snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)
            ]
        )
        if snake[0][0] == 0 or snake[0][0] == min_max[0] or snake[0][1] == 0 or snake[0][1] == min_max[1]:
            end_scene(scr)

        if snake[0] in snake[1:]:
            end_scene(scr)

        if score < 0:
            end_scene(scr)

        if snake[0] == food:                                            # When snake eats the food
            food = []
            score += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
                if food in snake:
                    food = []
            win.addch(food[0], food[1], '*')
        else:
            last = snake.pop()
            win.addch(last[0], last[1], ' ')
        win.addch(snake[0][0], snake[0][1], '•',)

        if snake[0] == enemy:
            enemy = []
            score -= 1
            while enemy == []:
                enemy = [randint(1, 18), randint(1, 58)]                 # Calculating next enemy's coordinates
                if enemy in snake:
                    enemy = []
            win.addch(enemy[0], enemy[1], '-')

    curses.endwin()


def multi_player(scr):  # Main multi player running
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    min_max = [curses.LINES, curses.COLS]
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    game_over = False

    key = KEY_RIGHT
    key2 = ord("d")
    global score_1                                                  # Initializing values
    score_1 = 0
    global score_2
    score_2 = 0
    global player_1
    player_1 = ""
    global player_2
    player_2 = ""

    snake_1 = [[4, 10], [4, 9], [4, 8]]                                     # Initial snake co-ordinates
    snake_2 = [[20, 14], [20, 13], [20, 12]]
    food = [10, 20]                                                    # First food co-ordinates

    win.addch(food[0], food[1], '*')                                   # Prints the food

    while key != 27:                             # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Player 1 score: ' + str(score_1) + ' ', curses.color_pair(2))
        win.addstr(0, 60, 'Player 2 score: ' + str(score_2) + ' ', curses.color_pair(1))
        win.addstr(0, 35, ' SNAKE ')
        win.timeout(80)

        prevKey = key
        prevKey2 = key2                                                 # Previous key pressed
        event = win.getch()

        if event != -1:
            key = event
            key2 = event

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey
        if prevKey == KEY_UP:
            if key in [KEY_DOWN]:
                key = prevKey
        if prevKey == KEY_DOWN:
            if key in [KEY_UP]:
                key = prevKey
        if prevKey == KEY_RIGHT:
            if key in [KEY_LEFT]:
                key = prevKey
        if prevKey == KEY_LEFT:
            if key in [KEY_RIGHT]:
                key = prevKey

        if key2 not in [27, ord("w"), ord("a"), ord("s"), ord("d")]:     # If an invalid key is pressed
            key2 = prevKey2
        if prevKey2 == ord("w"):
            if key2 in [ord("s")]:
                key2 = prevKey2
        if prevKey2 == ord("s"):
            if key2 in [ord("w")]:
                key2 = prevKey2
        if prevKey2 == ord("d"):
            if key2 in [ord("a")]:
                key2 = prevKey2
        if prevKey2 == ord("a"):
            if key2 in [ord("d")]:
                key2 = prevKey2

        snake_1.insert(
            0,
            [
                snake_1[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                snake_1[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)
                ]
        )
        snake_2.insert(
            0,
            [
                snake_2[0][0] + (key2 == ord("s") and 1) + (key2 == ord("w") and -1),
                snake_2[0][1] + (key2 == ord("a") and -1) + (key2 == ord("d") and 1)
            ]
        )

        if snake_1[0][0] == 0:  # goes up
            snake_1[0][0] = 22
        if snake_1[0][1] == 0:  # goes left
            snake_1[0][1] = min_max[0]+54
        if snake_1[0][0] == min_max[0]:
            snake_1[0][0] = 1
        if snake_1[0][1] == min_max[1]:
            snake_1[0][1] = 1

        if snake_2[0][0] == 0:  # goes up
            snake_2[0][0] = 22
        if snake_2[0][1] == 0:  # goes left
            snake_2[0][1] = min_max[0]+54
        if snake_2[0][0] == min_max[0]:
            snake_2[0][0] = 1
        if snake_2[0][1] == min_max[1]:
            snake_2[0][1] = 1

        if snake_1[0] in snake_1[1:]:
            multi_player_end_scene(scr)
        if snake_2[0] in snake_2[1:]:
            multi_player_end_scene(scr)

        global winner
        if snake_1[0] in snake_2[0:]:
            time.sleep(1)
            curses.endwin()
            multi_player_end_scene(scr)
        if snake_2[0] in snake_1[0:]:
            time.sleep(1)
            curses.endwin()
            multi_player_end_scene(scr)

        if snake_1[0] == food:                                            # When snake eats the food
            food = []
            score_1 += 1
            while food == []:
                food = [randint(1, 19), randint(1, 59)]                 # Calculating next food's coordinates
                if food in snake_1:
                    food = []
            win.addch(food[0], food[1], '*')
        else:
            last = snake_1.pop()
            win.addch(last[0], last[1], ' ')
        win.addch(snake_1[0][0], snake_1[0][1], '•', curses.color_pair(2))

        if snake_2[0] == food:                                            # When snake eats the food
            food = []
            score_2 += 1
            while food == []:
                food = [randint(1, 19), randint(1, 59)]                 # Calculating next food's coordinates
                if food in snake_2:
                    food = []
            win.addch(food[0], food[1], '*')
        else:
            last = snake_2.pop()
            win.addch(last[0], last[1], ' ')
        win.addch(snake_2[0][0], snake_2[0][1], '•', curses.color_pair(1))
        win.addch(0, 0, key2)
        win.refresh()

    end_scene(scr)

curses.wrapper(start_screen)
