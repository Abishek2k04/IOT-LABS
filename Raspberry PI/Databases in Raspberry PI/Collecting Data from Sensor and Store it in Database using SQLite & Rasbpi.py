import RPi.GPIO as GPIO
import time
import sqlite3
from datetime import datetime

# GPIO setup
GPIO.setmode(GPIO.BOARD)
TRIG = 31
ECHO = 18
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)

# Calibration
print("Calibrating...")
time.sleep(2)
print("Place Object")

# Trigger the ultrasonic burst
GPIO.output(TRIG, GPIO.HIGH)
time.sleep(0.00001)
GPIO.output(TRIG, GPIO.LOW)

# Measure pulse
while GPIO.input(ECHO) == 0:
    pulse_start = time.time()
while GPIO.input(ECHO) == 1:
    pulse_end = time.time()

# Calculate distance
pulse_duration = pulse_end - pulse_start
distance = round(pulse_duration * 17150 + 1.15, 2)

# Print and log if in range
if 5 <= distance <= 100:
    print("Distance:", distance, "cm")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = sqlite3.connect('sensordata.db')
    c = conn.cursor()
    query = f"INSERT INTO distances (timestamp, distance) VALUES ('{timestamp}', {distance})"
    c.execute(query)
    conn.commit()
    conn.close()

# Cleanup GPIO
GPIO.cleanup()
