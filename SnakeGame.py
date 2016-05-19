import curses
import sys
import time
import random
from random import randint
curses.initscr()

def add():
    input_file = open("name.txt", "a")
    name = input("enter your username: ")
    print(name, " ", score, file=input_file)
    input_file.close()

def print_score():
    output_file = open("name.txt", "r+")
    text_in_file = output_file.read()
    print(text_in_file)
    output_file.close()
    exit()



def end_scene(scr):
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
        main(scr)
    if event == ord("q"):
        curses.endwin()
        add()
        print_score()
    time.sleep(1)


def main(scr):
    curses.noecho()
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    curses.curs_set(0)
    min_max = win.getmaxyx()
    win.keypad(1)
    win.nodelay(0)
    win.border(0)
    title = ' Sneaky Game ! '                                                   #add to bounce right to left if we can
    win.addstr(0, (curses.COLS - len(title)) // 4, title)
    head = [15, 10]
    food = [10,20]
    enemy = [20,10]
    win.addch(food[0], food[1], '*')
    win.addch(enemy[0], enemy[1], '+')
    body = [head[:]]*5
    snake = head + body
    game_over = False
    direction = 0
    global score
    score = 0
    part = body[-1][:]
    messagne2 = str(len(body))

    while not game_over:
        win.timeout(90 - (len(body)+1))
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')# Printing score
        if score < 0:
            game_over = True
            end_scene(scr)


        if win.inch(head[0], head[1]) == ord("*"):
            food = []
            score += 1
            body.append(body[-1]*2)
            while food == []:
                food = [random.randint(1, 18), random.randint(1, 58)]   #Next food's coordinates
                if food in head: food = []
            win.addch(food[0], food[1], '*')

        if win.inch(head[0], head[1]) == ord("+"):
            enemy = []
            score -= 1
            while enemy == []:
                for enemy in range(3):
                    enemy = [random.randint(1, 18), random.randint(1, 58)]
                    win.addch(enemy[0], enemy[1], '+')


        if part not in body:
            win.addch(part[0], part[1], " ")
        win.addch(head[0], head[1], "X")

        movement = win.getch()
        if movement == curses.KEY_UP and direction != 1:
                direction = 3
        elif movement == curses.KEY_DOWN and direction != 3:
                direction = 1
        elif movement == curses.KEY_RIGHT and direction != 2:
                direction = 0
        elif movement == curses.KEY_LEFT and direction != 0:
                direction = 2


        if direction == 0:
            head[1] += 1
        elif direction == 2:
            head[1] -= 1
        elif direction == 1:
            head[0] += 1
        elif direction == 3:
            head[0] -= 1


        part = body[-1][:]
        for z in range(len(body)-1, 0, -1):
            body[z] = body[z-1]
        body[0] = head[:]

        if win.inch(head[0], head[1]) == ord("X"):
            game_over = True
            end_scene(scr)

        if head[1] == 0:
            game_over = True
            end_scene(scr)
        if head[0] == 0:
            game_over = True
            end_scene(scr)
        if head[1] == min_max[1]:
            game_over = True
            end_scene(scr)
        if head[0] == min_max[0]:
            game_over = True
            end_scene(scr)


        win.refresh()



curses.wrapper(main)
curses.endwin()
