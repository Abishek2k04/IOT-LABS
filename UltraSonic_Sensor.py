import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG = 31 	 	
ECHO = 18
i=0
GPIO.setup(TRIG,GPIO.OUT)#this for output from sensor
GPIO.setup(ECHO,GPIO.IN)#this for inout to sensor
GPIO.setup(TRIG,LOW)

print("calibring:")
time.sleep(2)
print("Place Object")

try:
    while True:
        GPIO.output(TRIG,HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG,LOW)
            
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
                
        while GPIO.input(ECHO)==1:
            pulese_end=time.time()
            
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*17150
        distance=round(distance+1.15,2)
             
        if distance <=30 and distance >=5:
            print("distance:",distance,"cm")
            print("object is near")
            i=1
                 
        if distance >30 and i==1:
            print("place the object....")
            i=0
            time.sleep(2)
except KeyboardInterrupt:
        print("Measurement stopped by user")
finally:
    GPIO.cleanup()
                 
