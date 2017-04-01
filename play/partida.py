# Based on Simon Game prototype by Piers Kennedy

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
from .partida_store import store_pontos, store_pontos_tempo

SAMPLERATE = 44100

RED     = 1
GREEN   = 2
YELLOW  = 3
BLUE    = 4

bluesound = '/tmp/blue.wav'
yellowsound = '/tmp/yellow.wav'
redsound = '/tmp/red.wav'
greensound = '/tmp/green.wav'
losingtone = '/tmp/losingtone.wav'

GPIOLED=[0,12,16,18,22]
GPIOSwitch=[0,7,11,13,15]

class Partida:
    def __init__(self):
        return

    @staticmethod
    def initGPIO():
        #Setup GPIO switches
        GPIO.setup(7, GPIO.IN)      #red    GPIO 7
        GPIO.setup(11, GPIO.IN)     #green  GPIO 0
        GPIO.setup(13, GPIO.IN)     #yellow GPIO 2
        GPIO.setup(15, GPIO.IN)     #blue   GPIO 3

        #Setup GPIO LEDs
        GPIO.setup(12, GPIO.OUT)    #red    GPIO 1
        GPIO.setup(16, GPIO.OUT)    #green  GPIO 4
        GPIO.setup(18, GPIO.OUT)    #yellow GPIO 5
        GPIO.setup(22, GPIO.OUT)    #blue   GPIO 6
        #Connect the ground to pin 6 and the positive to pin 1 (3V3)

    @staticmethod
    def initSound():
        pygame.mixer.pre_init(SAMPLERATE,-16,2,2048)
        pygame.mixer.init()
        subprocess.Popen('amixer cset numid=3 1', shell=True)

    @staticmethod
    def createSignal(frequency, duration):
        samples = int(duration * SAMPLERATE)
        period = SAMPLERATE / frequency
        omega = numpy.pi * 2 / period
        xaxis = numpy.arange(samples, dtype=numpy.float) * omega
        yaxis = 32800 * numpy.sin(xaxis)
        return yaxis.astype('int16').tostring()

    @staticmethod
    def createWAVFile(filename, signal):
        file = wave.open(filename, 'wb')
        file.setparams((1, 2, SAMPLERATE, len(signal), 'NONE',
        'noncompressed'))
        file.writeframes(signal)
        file.close()

    @staticmethod
    def playWAVFile(filename):
        sound = pygame.mixer.Sound(filename)
        sound.play()

    def initGame(self, velocidade, tam_sequencia):
        vel = float(velocidade)/10

        #blue sound 209Hz
        signal = Partida.createSignal(frequency=209, duration=vel)
        Partida.createWAVFile(bluesound, signal)

        #yellow sound 252Hz
        signal = Partida.createSignal(frequency=252, duration=vel)
        Partida.createWAVFile(yellowsound, signal)

        #red sound 310Hz
        signal = Partida.createSignal(frequency=310, duration=vel)
        Partida.createWAVFile(redsound, signal)

        #green sound 415Hz
        signal = Partida.createSignal(frequency=415, duration=vel)
        Partida.createWAVFile(greensound, signal)

        #losing tone 42 Hz
        signal = Partida.createSignal(frequency=42, duration=4)
        Partida.createWAVFile(losingtone, signal)

        # test-stuff
        # Partida.playWAVFile(bluesound)

        #Instance Variables
        self.max = tam_sequencia #No. of rounds in game
        self.RoundNo = 1
        self.correct = True
        self.sequence=[]
        for n in range(1,self.max+2):
            self.sequence.append(random.choice([RED, GREEN, YELLOW, BLUE]))

    @staticmethod
    def LEDout(val):
        if (val==RED):
            Partida.playWAVFile(redsound)
        elif (val==GREEN):
            Partida.playWAVFile(greensound)
        elif (val==YELLOW):
            Partida.playWAVFile(yellowsound)
        elif (val==BLUE):
            Partida.playWAVFile(bluesound)
        while pygame.mixer.get_busy():
            GPIO.output(GPIOLED[val], True)
        GPIO.output(GPIOLED[val], False)
        time.sleep(0.15)
        return[]

    @staticmethod
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

    @staticmethod
    def LoserLights():
        Partida.playWAVFile(losingtone)
        for cycle1 in range(0,6):
            for cycle2 in range(1,5):
                GPIO.output(GPIOLED[cycle2], True)
            time.sleep(0.5)
            for cycle2 in range(1,5):
                GPIO.output(GPIOLED[cycle2], False)
            time.sleep(0.2)
        return[]

    def executar(self, jogador_id):
        start = time.time()

        # test-stuff
        random_rounds = random.randint(1, 5)
        while self.RoundNo <= random_rounds:

        # while self.correct:
            print("Round %i" %self.RoundNo)
            #LED cycle
            for mout in range(1, self.RoundNo+1):
                Partida.LEDout(self.sequence[mout])
            #Response
            # for ans in range(1, self.RoundNo+1):
                # push=Partida.SwitchChosen()
                # Partida.LEDout(push)
                # if (push!=colour[ans]):
                #    Partida.LoserLights()
                #    self.correct = False
                #    # TODO: persist pontos, num_jogadas where id
                #    store_pontos(jogador_id, self.RoundNo-1)
                #    break
            self.RoundNo+=1
            # if (self.RoundNo==self.max+1):
            #     end = time.time()
            #     tempo = (end - start)
            #     # TODO: persist pontos, num_jogadas, tempo, menor_tempo where id
            #     store_pontos_tempo(jogador_id, self.RoundNo-1, tempo)
            #     break
            time.sleep(0.5)

        # test-stuff
        end = time.time()
        tempo = (end - start)
        print('tempo')
        print(tempo)
        store_pontos_tempo(jogador_id, self.RoundNo-1, tempo)
