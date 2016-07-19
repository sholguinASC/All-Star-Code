from random import *
from time import sleep

x = 350 #randint(20,670)
y = 350 #randint(20,670)
direction1 = randint(1,50)
direction2 = randint(1,5)
speed = 1

def setup(): 
  size(700, 700)
  background(233,52,52)

def draw():
    background(233,52,52)
    global x
    global y
    global speed
    global direction1
    global direction2
    x = x + speed*direction1
    y = y + speed*direction2
    if x < 20 or x > 675:
        direction1 = direction1 * -1
    if y < 20 or y > 675:
        direction2 = direction2 * -1
    #rotateY(-1.0)
    #rotateX(-1.0)
    noStroke()
    fill(31,190,222)
    ellipse(x,y,50,50)
    strokeWeight(4)
    
    
    rect(mouseX-70, 620, 140, 15)
    if x < mouseX - 70 and x < mouseX + 70:
        if y > 620 and y < 645:
            direction2 = direction2 * -1
