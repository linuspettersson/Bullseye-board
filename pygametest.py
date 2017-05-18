import sys
import tty
import termios
import time
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

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
freqInc = 20
sleepTime = 20
sleepTime2 = 20  ## Tested
freqInc2 = 200  ## Tested
runtime2 = 500
startFreq1 = 200
startFreq2 = 400
maxFreq1 = 1000
maxFreq2 = 4000 ## Somewhat tested

#########################################
#########################################

# Funtion to move motor 1
def move1(i):
    if (startFreq1+freqInc*i)<maxFreq1:
        p1.ChangeFrequency(startFreq1+freqInc*i)
    if (startFreq1+freqInc*i)> maxFreq1:
        p1.ChangeFrequency(maxFreq1)
        
# Function to move motor 2
def move2(i):
    if (startFreq2+freqI*i)<maxFreq2:
        p2.ChangeFrequency(startF2+freqInc2*i)
    if (startFreq2+freqInc2*i)> maxFreq2:
        p2.ChangeFrequency(maxFreq2)


#########################################
#########################################

wi = 0
si = 0
di = 0
ai = 0
pressed_w = False
pressed_a = False
pressed_s = False
pressed_d = False
pressed_UP = False
pressed_LEFT = False
pressed_DOWN = False
pressed_RIGHT = False
pygame.init()
FPSClock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        print('lol')
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Key input
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                p1.stop()
                p2.stop()
                GPIO.cleanup()
                pygame.quit()
                sys.exit()
            if event.key == K_w:
                if pressed_w == False:
                    print('Start\n')
                    GPIO.output(DirPin1,Up)
                    p1.ChangeDutyCycle(80)
                move(wi)
                wi=wi+1
                time.sleep(500/1000)
                pressed_w == True
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
                wi = 0
                p1.ChangeDutyCycle(100)
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
                
    if pressed_w == True & pressed_a == True:
        print('WAAAA')
    if pressed_w == True:
        move(wi)
        wi=wi+1
        time.sleep(20/1000)
        print('wi')
    elif pressed_a == True:
        print('a')
    elif pressed_s == True:
        print('s')
    elif pressed_d == True:
        print('d')
    x=pygame.event.Event(KEYDOWN,K_x)
    pygame.event.post(x)
    # if pressed_UP == True:
        #
    #if pressed_LEFT == True:
        #
    # if pressed_DOWN == True:
        #
    # if pressed_RIGHT == True:
        #
