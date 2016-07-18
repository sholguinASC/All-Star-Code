from random import *
from time import sleep
def setup(): 
  size(700, 700)

def draw():
    list1 = [randint(-75, 90), randint(-80,75)]
    list2 = [randint(-75, 90), randint(-90,75)]
    fill(randint(0,255),randint(0,255),randint(0,255))
    noStroke()
    ellipse(mouseX, mouseY, 80, 80) 
    for i  in range(15):
            w = randint(10, 30)
            ellipse(mouseX + choice(list1), mouseY + choice(list2), w, w)
            fill(randint(0,255),randint(0,255),randint(0,255)) 
            #sleep(.2) 
