import sys
import time
import RPi.GPIO as GPIO
from threading import Thread

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

freq1 = 250
runtime1 = 200
p1 = GPIO.PWM(PulsPin1,50)
p1.start(100)
p2 = GPIO.PWM(PulsPin2,50)
p2.start(100)
freqInc = 20
sleepTime = 10
sleepTime2 = 20  ## Tested
freqInc2 = 200  ## Tested
runtime2 = 500
startFreq1 = 200
startFreq2 = 300
maxFreq1 = 1000
maxFreq2 = 4000 ## Somewhat tested

def move(x,y):
    try:
        Thread(target=accelMove, args=(p1,maxFreq1,startFreq1,freqInc,sleepTime,y)).start()
        Thread(target=accelMove, args=(p2,maxFreq2,startFreq2,freqInc2,sleepTime2,x)).start()
    except Exception as e:
        print(e)
    
def accelMove(motor,maxF,startF,freqI,sleepT,runT):
    motor.ChangeDutyCycle(80)
    for i in range(0,runT,sleepT):
        f = i/sleepT
        if (startF+freqI*(f))>maxF:
            break
        motor.ChangeFrequency(startF+freqI*(f))
        time.sleep(sleepT/1000)
    if sleepT*f<=runT:
        time.sleep(runT/1000-(sleepT/1000)*f)
    motor.ChangeDutyCycle(100)
while True:
    statement = input('Enter your command\n')
    if statement in ('exit','Exit','c','close'):
        p1.stop()
        #p2.stop()
        GPIO.cleanup()
        break
    if statement in ('multi'):
        move(runtime2,runtime1)
    if statement in ('run','r'):
        mtor = input('What motor? 1:lower 2:upper\n')
        if mtor in ('upper','u'):
            accelMove(p2,maxFreq2,startFreq2,freqInc2,sleepTime2,runtime2)
        if mtor in ('lower','l'):
            accelMove(p1,maxFreq1,startFreq1,freqInc,sleepTime,runtime1)
        #time.sleep(runtime1/1000)
        p1.ChangeDutyCycle(100)
    if statement in ('time1'):
        runtime1 = int(input('Runtime1'))
    if statement in ('time2'):
        runtime2 = int(input('Runtime2'))
    if statement in ('change1','Change1'):
        #accSteps = int(input('Change number of acceleration steps\n'))
        freqInc = int(input('Change frequency increment\n'))
        sleepTime = int(input('Change time between steps\n'))
    if statement in ('dir','direction','Dir'):
        direction = input('Up or Down')
        if direction in ('Up','up'):
            GPIO.output(DirPin1,Up)
        if direction in ('Down','down'):
            GPIO.output(DirPin1,Down)
    if statement in ('change2','Change2'):
        #accSteps2 = int(input('Change number of acceleration steps\n'))
        freqInc2 = int(input('Change frequency increment\n'))
        sleepTime2 = int(input('Change time between steps\n'))
    if statement in ('dir2','direction2'):
        direction2 = input('Right or left\n')
        if direction2 in ('right','Right','r'):
            GPIO.output(DirPin2,Right)
        if direction2 in ('left','Left','l'):
            GPIO.output(DirPin2,Left)
                     
        
        




    
