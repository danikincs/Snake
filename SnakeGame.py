import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import sys
import time
import random
from random import randint
curses.initscr()


def add():                                    # Add .txt file if not exists, stores player score.
    input_file = open("name.txt", "a")
    name = input("enter your username: ")
    print(name, " ", score, file=input_file)
    input_file.close()


def print_score():                           # S hows score in terminal, previous scores also appears
    output_file = open("name.txt", "r+")
    text_in_file = output_file.read()
    print(text_in_file)
    output_file.close()
    exit()


def start_screen(scr):      # Start menu where you can choose single, or multiplayer game mode.
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win.clear()
    win.nodelay(0)
    message1 = "Welcome to the Sneaky Game !"
    message2 = "Press 1 to play Single Player, or Press 2 to play Multi Player!"
    win.addstr((curses.LINES) // 2, (curses.COLS - len(message1)) // 2, message1)
    win.addstr(((curses.LINES) // 2)+2, ((curses.COLS - len(message2)) // 2)+2, message2)
    event = win.getch()
    if event == ord("1"):
        single_player(scr)
    if event == ord("2"):
        multi_player(scr)


def end_scene(scr):                          # It appears, when player loses, replay or exit
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win.clear()
    win.nodelay(0)
    message1 = "Game Over!"
    message2 = "Press Q to quit, or Press P to Play Again!"
    message3 = "Your score is : " + str(score)
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
    time.sleep(1)


def multi_player_end_scene(scr):
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win.clear()
    win.nodelay(0)
    if winner == player_1:
        message1 = "Game Over!"
        win.addstr((curses.LINES) // 2, (curses.COLS - len(message1)) // 2, message1)
        message2 = "Player 1 won!"
        message3 = "Player 1 score is : " + str(score_1)
        win.addstr((curses.LINES) // 2, (curses.COLS - len(message1)) // 2, message1)
        win.addstr(((curses.LINES) // 2)+2, ((curses.COLS - len(message3)) // 2)+2, message3)
        event = win.getch()
        message4 = "Press Q to quit, or Press P to Play Again!"
        win.addstr(((curses.LINES) // 2)-2, ((curses.COLS - len(message4)) // 2), message4)
        if event == ord("p"):
            start_screen(scr)
        if event == ord("q"):
            curses.endwin()
            add()
            print_score()
        time.sleep(1)
    if winner == player_2:
        message1 = "Game Over!"
        win.addstr((curses.LINES) // 2, (curses.COLS - len(message1)) // 2, message1)
        message2 = "Player 2 won!"
        message3 = "Player 2 score is : " + str(score_2)
        win.addstr((curses.LINES) // 2, (curses.COLS - len(message2)) // 2, message2)
        win.addstr(((curses.LINES) // 2)+2, ((curses.COLS - len(message3)) // 2)+2, message3)
        event = win.getch()
        message4 = "Press Q to quit, or Press P to Play Again!"
        win.addstr(((curses.LINES) // 2)-2, ((curses.COLS - len(message4)) // 2), message4)
        if event == ord("p"):
            start_screen(scr)
        if event == ord("q"):
            curses.endwin()
            add()
            print_score()
        time.sleep(1)


def single_player(scr):
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    min_max = [curses.LINES, curses.COLS]
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    game_over = False

    key = KEY_RIGHT
    global score                                                  # Initializing values
    score = 0

    snake = [[4, 10], [4, 9], [4, 8]]                                     # Initial snake co-ordinates
    food = [10, 20]                                                     # First food co-ordinates

    win.addch(food[0], food[1], '*')                                   # Prints the food

    while key != 27 or game_over == False:                              # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
        win.timeout(90 - (len(snake)+1))          # Increases the speed of Snake as its length increases

        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event

        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        snake.insert(
            0,
            [
                snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)
            ]
        )

        if snake[0][0] == 0:  # goes up
            snake[0][0] = 22
        if snake[0][1] == 0:  # goes left
            snake[0][1] = min_max[0]+54
        if snake[0][0] == min_max[0]:
            snake[0][0] = 1
        if snake[0][1] == min_max[1]:
            snake[0][1] = 1

        if snake[0] in snake[1:]:
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
        win.addch(snake[0][0], snake[0][1], '#')

    curses.endwin()


def multi_player(scr):
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
    snake_2 = [[6, 14], [6, 13], [6, 12]]
    food = [10, 20]                                                    # First food co-ordinates

    win.addch(food[0], food[1], '*')                                   # Prints the food

    while key != 27:                             # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score_1) + ' ')                # Printing 'Score' and
        win.addstr(0, 66, 'Score_2 : ' + str(score_2) + ' ')
        win.addstr(0, 35, ' SNAKE ')                                   # 'SNAKE' strings
        win.timeout(60)

        prevKey = key
        prevKey2 = key2                                                 # Previous key pressed
        event = win.getch()

        if event != -1:
            key = event
            key2 = event

        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        if key2 not in [27, ord("w"), ord("a"), ord("s"), ord("d")]:     # If an invalid key is pressed
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
            end_scene(scr)
        if snake_2[0] in snake_2[1:]:
            end_scene(scr)
        if snake_1[0] in snake_2[0:]:
            global winner
            winner = player_2
            multi_player_end_scene(scr)
        if snake_2[0] in snake_1[0:]:
            global winner
            winner = player_1
            multi_player_end_scene(scr)

        if snake_1[0] == food:                                            # When snake eats the food
            food = []
            score_1 += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
                if food in snake_1:
                    food = []
            win.addch(food[0], food[1], '*')
        else:
            last = snake_1.pop()
            win.addch(last[0], last[1], ' ')
        win.addch(snake_1[0][0], snake_1[0][1], '#')

        if snake_2[0] == food:                                            # When snake eats the food
            food = []
            score_2 += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
                if food in snake_2:
                    food = []
            win.addch(food[0], food[1], '*')
        else:
            last = snake_2.pop()
            win.addch(last[0], last[1], ' ')
        win.addch(snake_2[0][0], snake_2[0][1], '+')
        win.addch(0, 0, key2)
        win.refresh()

    # curses.endwin()
    end_scene(scr)

curses.wrapper(start_screen)
