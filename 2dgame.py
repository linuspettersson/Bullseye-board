import pygame, sys, random, math
from pygame.locals import *

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
                    pressed_w = True
                if event.key == K_a:
                    pressed_a = True
                if event.key == K_s:
                    pressed_s = True
                if event.key == K_d:
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
                if event.key == K_a:
                    pressed_a = False
                if event.key == K_s:
                    pressed_s = False
                if event.key == K_d:
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
            car1.y += -1
        if pressed_a == True:
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

        pygame.display.update()
        FPSClock.tick(FPS)

if __name__=="__main__":
    main()
