import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Corrected to BOARD
GPIO.setup(3, GPIO.OUT)   # Corrected GPIO.OUT
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

while True:
    GPIO.output(5, GPIO.LOW)   # Corrected GPIO.LOW
    GPIO.output(3, GPIO.HIGH)  # Corrected GPIO.HIGH
    GPIO.output(7, GPIO.HIGH)
    time.sleep(.1)
    
    GPIO.output(3, GPIO.LOW)   # Corrected GPIO.LOW
    GPIO.output(7, GPIO.LOW)   # Corrected GPIO.LOW
    GPIO.output(5, GPIO.HIGH)
    time.sleep(.4)
    


GPIO.cleanup() # Added parentheses to cleanup

