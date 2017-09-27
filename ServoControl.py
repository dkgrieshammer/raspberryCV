import RPi.GPIO as GPIO
import pigpio
import time

class servoControl:
    SERVO_PIN = 17
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(SERVO_PIN, GPIO.OUT)
##    p = GPIO.PWM(SERVO_PIN, 50); # We define servopin as PWM Pin with 50Hz
    pi = pigpio.pi()
    
    def __init__(self):
        self.pi.set_servo_pulsewidth(self.SERVO_PIN, 2000) #init
        return

    def setPos(self,pos):
##        pos = 3000 - float(pos)
        pos = float(pos)
##        print(pos)
        self.pi.set_servo_pulsewidth(self.SERVO_PIN,pos)
##        time.sleep(stime)
    
    def kill(self):
        print("kill called")
##        self.p.stop()
##        GPIO.cleanup()
        

