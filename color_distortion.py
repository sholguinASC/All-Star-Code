from Myro import*

pic = makePicture("flic.jpg")
show(pic)

DarkBlue = makeColor(0,51,76)

Red = makeColor(217, 26, 33)

Blue = makeColor(112,150,158)

Yellow = makeColor(252, 227, 166)

for i in getPixels(pic):
    getRed(i)
    getGreen(i)
    getBlue(i)
    #makeColor(RED,GREEN,BLUE)
