def colorRecognizer(colur):
    if colur == "Blue":
        return 0,0,255
    if colur == "Red":
        return 255,0,0
    if colur == "Yellow":
        return 0,0,0
    if colur == "Green":
        return 0,255,0

def makeCar(body_color, wheel_color, rod_color, seat_color):
    #Body of car
    fill(0,0,255)
    rect(30, 120, 255, 55, 0, 20, 20, 0) 
    #All the 4 wheels of the car
    fill(0)
    ellipse(50,90,55,55)
    ellipse(50,205,55,55)
    ellipse(260,90,55,55)
    ellipse(260,205,55,55)
    #Rods holding the wheel of the car
    fill(255,0,0)
    rect(47,105,9,90)
    rect(257,105,9,90)
    #Driver's Seat
    fill(0,200,0)
    rect(80,125,60,45)
         
    
size(300,300)
    
makeCar(blue)
