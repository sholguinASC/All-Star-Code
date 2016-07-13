from Myro import *
init("sim")
sim = Simulation("Empty Room",700,700, makeColor("blue"))
sim.setup()
makeRobot("SimScribbler",sim)

def drawL(x):
    penDown()
    forward(1, 2*x)
    penUp()

def drawH(y):
    penDown()
    forward(1, 2*y)
    penUp()
    backward(1, 1*y)
    penDown()
    turnBy(90,"deg")
    forward(1, 1*y)
    turnBy(90,"deg")
    backward(1, 1*y)
    forward(1, 2*y)
    penUp()
#-------------------------
Size = 2    
#-------------------------
turnBy(-90,"deg")    
drawL(Size)
turnBy(90,"deg")
forward(1,2*Size)
turnBy(90,"deg")
drawH(Size)
forward(1,2*Size)
