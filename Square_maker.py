from Myro import *
init("sim")
sim = Simulation("Empty Room",700,700, makeColor("green"))
sim.setup()
makeRobot("SimScribbler",sim)
length = int(raw_input("How big do you want the square? "))
penDown()
for i in range(3):
  for i in range(3):
    forward(1,length)
    turnBy(90,"deg")
  forward(1,length)
  length = length*1.5
