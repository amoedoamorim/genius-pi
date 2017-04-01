##!/usr/bin/env python
#______________________________
#
#Simon Game prototype
#Piers Kennedy
#12-07-2012 (update 27-02-2013)
#
#______________________________

import RPi.GPIO as GPIO
import sys
import random
import time
import numpy
import wave
import pygame
import subprocess
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

vel = float(sys.argv[1])
vel = vel/10


#Set up sounds
#This avoids any delay before sound starts
pygame.mixer.pre_init(44100,-16,2,2048)
#Initialise mixer
pygame.mixer.init()
subprocess.Popen('amixer cset numid=3 1',shell=True)
SAMPLERATE = 44100

def createSignal(frequency, duration):
    samples = int(duration*SAMPLERATE)
    period = SAMPLERATE / frequency
    omega = numpy.pi * 2 / period
    xaxis = numpy.arange(samples, dtype=numpy.float) * omega
    yaxis = 32800 * numpy.sin(xaxis)
    return yaxis.astype('int16').tostring()

def createWAVFile(filename, signal):
    file = wave.open(filename, 'wb')
    file.setparams((1, 2, SAMPLERATE, len(signal), 'NONE',
    'noncompressed'))
    file.writeframes(signal)
    file.close()

def playWAVFile(filename):
    sound = pygame.mixer.Sound(filename)
    sound.play()

#blue sound 209Hz
bluesound = '/tmp/blue.wav'
signal = createSignal(frequency=209, duration=vel)
createWAVFile(bluesound, signal)
#yellow sound 252Hz
yellowsound = '/tmp/yellow.wav'
signal = createSignal(frequency=252, duration=vel)
createWAVFile(yellowsound, signal)
#red sound 310Hz
redsound = '/tmp/red.wav'
signal = createSignal(frequency=310, duration=vel)
createWAVFile(redsound, signal)
#green sound 415Hz
greensound = '/tmp/green.wav'
signal = createSignal(frequency=415, duration=vel)
createWAVFile(greensound, signal)

#losing tone 42 Hz
losingtone = '/tmp/losingtone.wav'
signal = createSignal(frequency=42, duration=3)
createWAVFile(losingtone, signal)

#Variables
max     = int(sys.argv[2])       #No. of rounds in game
RoundNo = 1
RED     = 1
GREEN   = 2
YELLOW  = 3
BLUE    = 4
correct = True

#Setup GPIO switches
GPIOSwitch=[0,7,11,13,15]
GPIO.setup(7, GPIO.IN)      #red    GPIO 7
GPIO.setup(11, GPIO.IN)     #green  GPIO 0
GPIO.setup(13, GPIO.IN)     #yellow GPIO 2
GPIO.setup(15, GPIO.IN)     #blue   GPIO 3

#Setup GPIO LEDs
GPIOLED=[0,12,16,18,22]
GPIO.setup(12, GPIO.OUT)    #red    GPIO 1
GPIO.setup(16, GPIO.OUT)    #green  GPIO 4
GPIO.setup(18, GPIO.OUT)    #yellow GPIO 5
GPIO.setup(22, GPIO.OUT)    #blue   GPIO 6

#Connect the ground to pin 6 and the positive to pin 1 (3V3)

#Generate a random list of LED outputs
colour=[]
for n in range(1,max+2):
    colour.append(random.choice([RED,GREEN,YELLOW,BLUE]))

#Function to switch LEDs on then off
def LEDout(val):
    if (val==RED):
        playWAVFile(redsound)
    elif (val==GREEN):
        playWAVFile(greensound)
    elif (val==YELLOW):
        playWAVFile(yellowsound)
    elif (val==BLUE):
        playWAVFile(bluesound)
    while pygame.mixer.get_busy():
        GPIO.output(GPIOLED[val], True)
    GPIO.output(GPIOLED[val],False)
    time.sleep(0.15)
    return[]

#Function to check when switch is pressed
def SwitchChosen():
    while True:
            if (GPIO.input(GPIOSwitch[RED])):
                return RED
            if (GPIO.input(GPIOSwitch[GREEN])):
                return GREEN
            if (GPIO.input(GPIOSwitch[YELLOW])):
                return YELLOW
            if (GPIO.input(GPIOSwitch[BLUE])):
                return BLUE

#Function to flash LEDs after mistake
def LoserLights():
    playWAVFile(losingtone)
    for cycle1 in range(0,6):
        for cycle2 in range(1,5):
            GPIO.output(GPIOLED[cycle2], True)
        time.sleep(0.5)
        for cycle2 in range(1,5):
            GPIO.output(GPIOLED[cycle2], False)
        time.sleep(0.2)
    return[]

#Main routine
while correct:
    print("Round %i" %RoundNo)
    #LED cycle
    for mout in range(1,RoundNo+1):
        LEDout(colour[mout])
    #Response
    for ans in range(1,RoundNo+1):
        push=SwitchChosen()
        LEDout(push)
        if(push!=colour[ans]):
            LoserLights()
            correct = False
            print("Unlucky!")
            print("You made it to round %i" %RoundNo)
            # TODO: persist pontos, num_jogadas where id
            break
    RoundNo+=1
    if (RoundNo==max+1):
        print("WOW!! You Rock dude")
        # TODO: persist pontos, num_jogadas, tempo, menor_tempo where id
        break
    time.sleep(0.5)
