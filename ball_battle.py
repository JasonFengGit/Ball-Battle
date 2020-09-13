import pygame as pg
from pygame.locals import *
from time import sleep
import sys
import random

pg.init()
scr=pg.display.set_mode((600,400))
pg.display.set_caption("ball battle")
pg.display.set_icon(scr)

zt24=pg.font.SysFont('stkaiti',24)
zt40=pg.font.SysFont('stkaiti',40)
zt30=pg.font.SysFont('stkaiti',30)

def printtext(font,text,x,y,color):
   img=font.render(text,True,color)
   scr.blit(img,(x,y))

def draw_p(p1_y, p2_y):
    speed = 2
    keys = pg.key.get_pressed()
    if keys[K_w]:
        p1_y -= speed
        p1_y = max(0, p1_y)
    elif keys[K_s]:
        p1_y += speed
        p1_y = min(350, p1_y)
    if keys[K_UP]:
        p2_y -= speed
        p2_y = max(0, p2_y)
    elif keys[K_DOWN]:
        p2_y += speed
        p2_y = min(350, p2_y)
    pg.draw.rect(scr,(255,255,255),(100,p1_y,10,50),0)
    pg.draw.rect(scr,(255,255,255),(490,p2_y,10,50),0)
    return (p1_y, p2_y)

def draw_socre_zone():
    pg.draw.rect(scr,(255,255,255),(0,0,80,75),0)
    pg.draw.rect(scr,(255,255,255),(0,325,80,75),0)
    pg.draw.rect(scr,(255,255,255),(520,0,80,75),0)
    pg.draw.rect(scr,(255,255,255),(520,325,80,75),0)

def init_ball(ball_speed):
    pg.draw.circle(scr,(255,255,255),(300,200), 7)

    vx = random.randint(-ball_speed, ball_speed)
    vy = random.randint(-ball_speed, ball_speed)
    while vx == 0:
        vx = random.randint(-ball_speed, ball_speed)
    while vy == 0:
        vy = random.randint(-ball_speed, ball_speed)
    return 300, 200, vx, vy

def in_wall(x, y):
    return (y in range(75) and x in range(80)) or (y in range(325,400) and x in range(80)) or (y in range(325,400) and x in range(520, 600)) or (y in range(75) and x in range(520, 600))

def in_p(x, y, p1_y, p2_y):
    if x in range(100, 110):
        return y in range(p1_y, p1_y + 50)
    elif x in range(490, 500):
        return y in range(p2_y, p2_y + 50)
def update_ball(x, y, vx, vy, p1_y, p2_y):
    x += vx
    y += vy

    if x < 0 or x > (600 - 7) or in_wall(x, y) or in_p(x, y, p1_y, p2_y):
        vx = -vx
    if y < 0 or y > (400 - 7):
        vy = -vy
    pg.draw.circle(scr,(255,255,255),(x, y), 7)
    return x, y, vx, vy

def main_loop():
    c_x, c_y = 0, 0
    p1_y, p2_y = 200, 200
    p1 = 0
    p2 = 0
    b_x, b_y = -1, -1
    while True:
        if p1 >= 6 or p2 >= 6:
            break
        scr.fill((0,0,0))
        for eve in pg.event.get():
            if eve.type == QUIT:
                sys.exit()
        keys = pg.key.get_pressed()
        p1_y, p2_y = draw_p(p1_y, p2_y)
        draw_socre_zone()
        printtext(zt30, "Player 1: " + str(p1), 100, 10, (255,255,255))
        printtext(zt30, "Player 2: " + str(p2), 370, 10, (255,255,255))
        printtext(zt24, "press R to serve again", 200, 30, (255,255,255))
        if (b_x == -1 and b_y) == -1 or keys[K_r]:
            b_x, b_y, vx, vy = init_ball(2)
            #print(b_x, b_y)
        else:
            b_x, b_y, vx, vy = update_ball(b_x, b_y, vx, vy, p1_y, p2_y)
        if b_x in range(0,80) and b_y in range(75, 325):
            p2 += 1
            #sleep(1)
            printtext(zt30, "Player 2 got 1 point!", 220, 200, (255,255,255))
            pg.display.update()
            sleep(1.5)
            b_x, b_y, vx, vy = init_ball(2)
        elif b_x in range(520,600) and b_y in range(75, 325):
            p1 += 1
            #sleep(1)
            printtext(zt30, "Player 1 got 1 point!", 220, 200, (255,255,255))
            pg.display.update()
            sleep(1.5)
            b_x, b_y, vx, vy = init_ball(2)
        pg.display.update()
        sleep(0.005)
    scr.fill((0,0,0))
    printtext(zt40, "Player %d got 1 point!"%(1 if p1 > p2 else 2), 220, 200, (255,255,255))
    printtext(zt30, "press R to restart", 200, 30, (255,255,255))
    pg.display.update()
    keys = pg.key.get_pressed()
    scr.fill((0,0,0))
    while not keys[K_r]:
        for eve in pg.event.get():
            if eve.type == QUIT:
                sys.exit()
        keys = pg.key.get_pressed()
        printtext(zt40, "Player %d WIN!!! Woooo Lololo"%(1 if p1 > p2 else 2), 130, 200, (255,255,255))
        printtext(zt30, "press R to restart", 200, 30, (255,255,255))
        pg.display.update()
while True: 
    main_loop()
