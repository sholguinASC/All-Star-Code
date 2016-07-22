from random import randint, choice

playerX = 250
xSpeed = 5
count = 0

shootX = 0
shootY = 0

enemyX = 0
enemyY = 550

gameStatus = 0

enemyList = [
    #[ original, health, x, y]
    [1, 50, 50],
    [1, 100, 50],
    [1, 150, 50],
    [1, 200, 50],
    [1, 250, 50],
    [1, 300, 50],
    [1, 350, 50],
    [1, 400, 50],
    [1, 450, 50],
    [1, 50, 100],
    [1, 100, 100],
    [1, 150, 100],
    [1, 200, 100],
    [1, 250, 100],
    [1, 300, 100],
    [1, 350, 100],
    [1, 400, 100],
    [1, 450, 100],
    [1, 50, 150],
    [1, 100, 150],
    [1, 150, 150],
    [1, 200, 150],
    [1, 250, 150],
    [1, 300, 150],
    [1, 350, 150],
    [1, 400, 150],
    [1, 450, 150],
    [1, 50, 200],
    [1, 100, 200],
    [1, 150, 200],
    [1, 200, 200],
    [1, 250, 200],
    [1, 300, 200],
    [1, 350, 200],
    [1, 400, 200],
    [1, 450, 200]
]

def setup():
    size(500, 500)
    background(0)
    
    rectMode(CENTER)
    ellipseMode(CENTER)
    noStroke()
    
def draw():
    global playerX
    global enemyList
    
    global gameStatus
    
    global shootX
    global shootY
    
    global enemyX
    global enemyY
    
    background(0)
    
    #Draw Player
    fill(0, 250, 0)
    rect(playerX, 400, 60, 30, 20, 20,0,0)
    fill(0, 250, 0)
    rect(playerX, 380, 10, 30)
    
    #Draw Projectile
    fill(0, 250, 0)
    shootY = shootY - 3
    rect(shootX, shootY, 5, 15)
    
    #Draw EnemyShot
    fill(255, 0, 0)
    enemyY = enemyY + 3
    rect(enemyX, enemyY, 5, 15)
    
    if enemyX <= playerX + 30 and enemyX >= playerX - 30 and enemyY >= 370 and enemyY <= 430:
        print("yaaa")
        
    #Draw Enemies
    for x in enemyList:
        fill(255, 0, 0)
        rect(x[1], x[2], 30, 30)
        
        if shootX <= x[1] + 10 and shootX >= x[1] - 10 and shootY <= x[2] + 10 and shootY >= x[2] - 10:
            print('destroy')
            shootY = -50
            
            enemyList.remove(x)
    
    if enemyY >= 550:
        if randint(0, 100) < 20:
            maxY = 0
            chosenX = []
        
            for x in enemyList:
                if maxY < x[2]:
                    maxY = x[2]
                    chosenX = []
                    chosenX.append(x[1])
                elif maxY == x[2]:
                    chosenX.append(x[1])
                
            enemyX = choice(chosenX)
            enemyY = maxY        
    
def keyPressed():
    global playerX
    global xSpeed
    global shootX
    global shootY
    
    if key == CODED:
        if keyCode == LEFT:
            playerX = playerX - xSpeed
        elif keyCode == RIGHT:
            playerX = playerX + xSpeed
        elif keyCode == UP:
            if shootY <= 0:
                shootX = playerX
                shootY = 400
