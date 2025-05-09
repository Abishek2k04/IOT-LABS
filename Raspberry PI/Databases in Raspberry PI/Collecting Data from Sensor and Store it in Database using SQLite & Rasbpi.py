import RPi.GPIO as GPIO
import time
import sqlite3
from datetime import datetime
GPIO.setmode(GPIO.BOARD)
TRIG = 31
ECHO = 18
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
print("Calibrating...")
time.sleep(2)
print("Place Object")
def log_distance(distance):
    conn = sqlite3.connect('sensordata.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO distances (timestamp, distance) VALUES (?, ?)", (timestamp, distance))
    conn.commit()
    conn.close()
try:
    while True:
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = round(pulse_duration * 17150 + 1.15, 2)
 

        if 5 <= distance <= 100:  # Adjust max distance as needed
            print("Distance:", distance, "cm")
            log_distance(distance)
        time.sleep(1)  # Adjust sampling rate
except KeyboardInterrupt:
    print("Measurement stopped by user")
finally:
    GPIO.cleanup()
