import pygame, sys, random, math
from pygame.locals import *
import time
import RPi.GPIO as GPIO



######################## Setup For GPIO
#Use Board References
GPIO.setmode(GPIO.BOARD)

PulsPin1 = 13
DirPin1 = 18
PulsPin2 = 12
DirPin2 = 16

Up = False
Down = True
Right = True
Left = False
GPIO.setwarnings(False)
GPIO.setup(PulsPin1,GPIO.OUT)
GPIO.setup(DirPin1,GPIO.OUT)
GPIO.setup(PulsPin2,GPIO.OUT)
GPIO.setup(DirPin2,GPIO.OUT)
GPIO.output(PulsPin1,True)
GPIO.output(DirPin1,Down)
GPIO.output(PulsPin2,True)
GPIO.output(DirPin2,Right)

###################################### Motor control parameters
######################################

freq1 = 250
runtime1 = 200
p1 = GPIO.PWM(PulsPin1,0.1)
p1.start(100)
p2 = GPIO.PWM(PulsPin2,0.1)
p2.start(100)
freqInc = 44
sleepTime = 20
sleepTime2 = 20  ## Tested
freqInc2 = 200  ## Tested
runtime2 = 500
startFreq1 = 400
startFreq2 = 600
maxFreq1 = 1000
maxFreq2 = 4000 ## Somewhat tested
Run1 = False
Run2 = False
wi=0
si=0
di=0
ai=0
#########################################
#########################################

# Funtion to move motor 1
def move1():
    #integer = 0
    #while Run1 == True:
        #if (startFreq1+freqInc*i)<maxFreq1:
    p1.ChangeFrequency(startFreq1)
        #if (startFreq1+freqInc*i)> maxFreq1:
        #    p1.ChangeFrequency(maxFreq1)
        #integer = integer+1
        #time.sleep(20/1000)
        
# Function to move motor 2
def move2():
    p2.ChangeFrequency(startFreq2)
    #if (startFreq2+freqInc2*i)<maxFreq2:
    #   p2.ChangeFrequency(startFreq2+freqInc2*i)
    #if (startFreq2+freqInc2*i)> maxFreq2:
    #    p2.ChangeFrequency(maxFreq2)



#########################################
#########################################
#Global variables
#nameOfPlayer = input("Enter your nick: ")
windowWidth = 800
windowHeight = 600
roadWidth = 50
carWidth = 10
carLength = 10
#roadLines[[(100,100),(700,100)],[(675,76),(675,200)]]
#Frames per second, changes the speed of the game
FPS = 300

#Colors
roadColor = (64,64,64)
groundColor = (21,249,28)
lineColor = (255,255,255)
car1Color = (255,255,0)
car2Color = (255,0,0)

#Draws the window
def drawMap():
    #Fill the map with color of ground
    displaySurf.fill(groundColor)
    #Square road
    pygame.draw.line(displaySurf, roadColor,(100,100),(700,100),roadWidth)
    pygame.draw.line(displaySurf, roadColor,(675,76) ,(675,500),roadWidth)
    pygame.draw.line(displaySurf, roadColor,(700,475),(100,475),roadWidth)
    pygame.draw.line(displaySurf, roadColor,(100,500),(100,76),roadWidth)
    pygame.draw.line(displaySurf, lineColor,(398,100),(402,100),roadWidth)

#Draws the car nr 1
def drawCar1(car):
    #Stops car going out of the map
    if car.bottom > windowHeight:
        car.bottom = windowHeight
    elif car.top < 0:
        car.top = 0
    elif car.left < 0:
        car.left = 0
    elif car.right > windowWidth:
        car.right = windowWidth
    pygame.draw.rect(displaySurf,car1Color, car)

#Draws the car nr 2
def drawCar2(car):
    #Stops car going out of the map
    if car.bottom > windowHeight:
        car.bottom = windowHeight
    elif car.top < 0:
        car.top = 0
    elif car.left < 0:
        car.left = 0
    elif car.right > windowWidth:
        car.right = windowWidth
    pygame.draw.rect(displaySurf,car2Color, car)
    
def main():
    pygame.init()
    global displaySurf
    
    FPSClock = pygame.time.Clock()
    displaySurf = pygame.display.set_mode((windowWidth,windowHeight))
    pygame.display.set_caption("2D cart game")

    #Initial variables
    car1X = 385
    car1Y = 97-carLength
    car2X = 385
    car2Y = 98+carWidth
    pressed_w = False
    pressed_a = False
    pressed_s = False
    pressed_d = False
    pressed_UP = False
    pressed_LEFT = False
    pressed_DOWN = False
    pressed_RIGHT = False

    wi=0
    si=0
    di=0
    ai=0
    #Creates rectangle for car
    car1 = pygame.Rect(car1X,car1Y,carLength,carWidth)
    car2 = pygame.Rect(car2X,car2Y,carLength,carWidth)

    #Draws the initial circuit
    drawMap()
    drawCar1(car1)
    drawCar2(car2)

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Key input
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_w:
                    if pressed_w == False:
                        GPIO.output(DirPin1,Up)
                        p1.ChangeDutyCycle(80)
                    Run1 = True
                    move1()
                    #wi=wi+1
                    pressed_w = True
                if event.key == K_a:
                    if pressed_a == False:
                        GPIO.output(DirPin2,Left)
                        p2.ChangeDutyCycle(80)
                    move2()
                    ai=ai+1
                    pressed_a = True
                if event.key == K_s:
                    if pressed_s == False:
                        GPIO.output(DirPin1,Down)
                        p1.ChangeDutyCycle(80)
                    pressed_s = True
                    move1()
                    si=si+1
                if event.key == K_d:
                    if pressed_d == False:
                        GPIO.output(DirPin2,Right)
                        p2.ChangeDutyCycle(80)
                    move2()
                    di=di+1
                    pressed_d = True
                if event.key == K_UP:
                    pressed_UP = True
                if event.key == K_LEFT:
                    pressed_LEFT = True
                if event.key == K_DOWN:
                    pressed_DOWN = True
                if event.key == K_RIGHT:
                    pressed_RIGHT = True
            if event.type == KEYUP:
                if event.key == K_w:
                    pressed_w = False
                    Run1 =False
                    p1.ChangeDutyCycle(100)
                    wi=0
                if event.key == K_a:
                    p2.ChangeDutyCycle(0)
                    ai=0
                    pressed_a = False
                if event.key == K_s:
                    p1.ChangeDutyCycle(0)
                    si=0
                    pressed_s = False
                if event.key == K_d:
                    p2.ChangeDutyCycle(0)
                    di=0
                    pressed_d = False
                if event.key == K_UP:
                    pressed_UP = False
                if event.key == K_LEFT:
                    pressed_LEFT = False
                if event.key == K_DOWN:
                    pressed_DOWN = False
                if event.key == K_RIGHT:
                    pressed_RIGHT = False

        if pressed_w == True:
            wi= wi+1
            car1.y += -1
        if pressed_a == True:
            ai+=1
            car1.x += -1
        if pressed_s == True:
            car1.y += 1
        if pressed_d == True:
            car1.x += 1
        if pressed_UP == True:
            car2.y += -1
        if pressed_LEFT == True:
            car2.x += -1
        if pressed_DOWN == True:
            car2.y += 1
        if pressed_RIGHT == True:
            car2.x += 1

        #Updating the circuit
        drawMap()
        drawCar1(car1)
        drawCar2(car2)
        #time.sleep(50/1000)
        pygame.display.update()
        FPSClock.tick(300)

if __name__=="__main__":
    main()
