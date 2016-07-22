from random import *
from time import sleep 

def setup():
    size(800, 300)
    background(255,0,0)
        
def randomLetter():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    randletter = choice(alphabet)
    
    print(randletter)
    sleep(1)
    return randletter

def checkPressed(H):
    global score
    if keyPressed:
        if key == H or key == H.upper():
            fill(0)
            score = score + 1
            sleep(0)
            print("pressed")
        else:
            score = score - 1
            sleep(0)
            
screenLetters = []
wait = 0

def draw():
    global score
    global i
    global screenLetters
    global wait
    
    if wait == 0:
        wait = 0
        screenLetters.append([randomLetter(),0, 150])
    wait = wait + 1

    background(255,0,0)
    fill(0)
    textSize(36)
    
    for x in range(len(screenLetters)):
        text(letter,screenLetters[x ][1],150)
    
    checkPressed(L)
    fill(0,255,0)
    text("Score: " +str(score), 50,50)
    i = i + 10
    sleep(0.1)
