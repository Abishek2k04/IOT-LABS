import RPi.GPIO as GPIO
import time

#ervoPIN=11
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

p=GPIO.PWM(11,100)
p.start(0)
while True:
    p.ChangeDutyCycle(0)
    time.sleep(0.5)

    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    
    p.ChangeDutyCycle(15)
    time.sleep(0.5)
    
    p.ChangeDutyCycle(20)
    time.sleep(0.5)

    p.ChangeDutyCycle(25)
    time.sleep(0.5)
    
    p.ChangeDutyCycle(30)
    time.sleep(0.5)
    
    p.ChangeDutyCycle(5)
    time.sleep(0.5)

    p.ChangeDutyCycle(0)
    time.sleep(0.5)

p.stop()
GPIO.cleanup()