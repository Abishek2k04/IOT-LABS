import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Corrected to BOARD
GPIO.setup(3, GPIO.OUT)

while True:
        print("LIGHT_ON")
        GPIO.output(3, GPIO.HIGH)  # Corrected GPIO.HIGH
        time.sleep(1)
        print("LIGHT_OFF")
        GPIO.output(3, GPIO.LOW)   # Corrected GPIO.LOW
        time.sleep(1)
    
GPIO.cleanup