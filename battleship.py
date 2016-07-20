from random import *
from time import sleep
def check_x():
    return  mouseX/100

def check_y():
    return mouseY/100

def check_win():
    global count
    global win
    if win == 1:
        background(0,255,0)
        textSize(70)
        text("YOU WIN", 92, 250)
    if count > 4:
        background(0,0,0)
        textSize(70)
        text("YOU LOSE", 85, 250)

def checkPosition(a,c):
    global win
    global count
    if list[a][c] == 1:
        fill(200,55,123)
        ellipse(a*100 + 50,c*100 + 50,100,100)
        win = 1
    else:
        fill(255,0,0)
        rect(a*100,c*100,100,100) 
        count = count + 1

def setup():
    size(500,500)
    for s in [0,1,2,3,4]:
        for b in [0,1,2,3,4]:
            fill(value, b*100,s*30)
            rect(b*100,s*100,100,100)  

value = 0    
list= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
list[randint(0,4)][randint(0,4)] = 1
win = 0
count = 0

def draw():
            if mousePressed:
                checkPosition(check_x(),check_y())
                check_win()
                print count
                sleep(.2)
