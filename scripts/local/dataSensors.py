import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os

class dataSensors:

    listaValues = []

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    
    def __init__(self, listaValues=list()):
        self.listaValues = listaValues
    
    def us(self, sensor):
        TRIG = sensor.pin[0] #25 
        ECHO = sensor.pin[1] #24
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, True)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == False:
            start = time.time()
        while GPIO.input(ECHO) == True:
            end = time.time()
        sig_time = end - start
        distancia = sig_time / 0.000058
        #distancia2 = sig_time / 0.000148
        #print('\nDistancia : {} centimetros'.format(distancia))
        #print('Distancia 2: {} pulgadas'.format(distancia2))
        return distancia
        
    
    def thInterna(self, sen):
        sensor = Adafruit_DHT.DHT11
        pin = sen.pin[0] #22
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        print('\nHumedad: {}'.format(humedad))
        print('Temperatura: {}'.format(temperatura))
        time.sleep(1)
    
    def thExterna(self):
        sensor = Adafruit_DHT.DHT11
        pin = 17
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        print('\nHumedad: {}'.format(humedad))
        print('Temperatura: {}'.format(temperatura))
        time.sleep(1)

    def pir(self):
        GPIO_PIR = 18
        GPIO.setup(GPIO_PIR, GPIO.IN)
        if GPIO.input(GPIO_PIR):
            print('\nSe detecto una presencia')
        else:
            print('\nNo hay presencia')
        time.sleep(1)
    
    def gh(self):
        pin1 = 20
        pin2 = 21
        GPIO.setup(pin1, GPIO.IN)
        GPIO.setup(pin2, GPIO.OUT)
        if GPIO.input(pin1):
            print('\nSin problemas')
        elif GPIO.input(pin1) != 1:
            print('\nSe a detectado presencia de humo o de gas')
            GPIO.output(pin2, False)
            time.sleep(1)
            GPIO.output(pin2, True)
        time.sleep(1)
