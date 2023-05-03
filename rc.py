from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

enableA = 25
input1 = 23
input2 = 24

enableB = 2
input3 = 3
input4 = 4

sensorInputRight = 16
sensorInputLeft = 21

GPIO.setmode(GPIO.BCM) # Use GPIO numbering instead of physical numbering

# Motor A
GPIO.setup(enableA, GPIO.OUT)
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)

# Motor B
GPIO.setup(enableB, GPIO.OUT)
GPIO.setup(input3, GPIO.OUT)
GPIO.setup(input4, GPIO.OUT)

# Sensors
GPIO.setup(sensorInputRight, GPIO.IN)
GPIO.setup(sensorInputLeft, GPIO.IN)

pwmA = GPIO.PWM(enableA, 100)
pwmA.start(0)
pwmB = GPIO.PWM(enableB, 100)
pwmB.start(0)


while True:
    state_sensorLeft = GPIO.input(sensorInputLeft)
    state_sensorRight = GPIO.input(sensorInputRight)
    
    
    
    # Both sensors detect black tape, stop car  
    if (state_sensorLeft == True and state_sensorRight == True):
        GPIO.output(input3,GPIO.LOW)
        GPIO.output(input4,GPIO.LOW)
        pwmB.ChangeDutyCycle(0)
        GPIO.output(input1,GPIO.LOW)
        GPIO.output(input2,GPIO.LOW)
        pwmA.ChangeDutyCycle(0)    
        
    # Only right sensor detects black tape, turn right
    if (state_sensorLeft == False and state_sensorRight == True):
        GPIO.output(input3,GPIO.LOW)
        GPIO.output(input4,GPIO.HIGH)
        pwmB.ChangeDutyCycle(85)
        GPIO.output(input1,GPIO.LOW)
        GPIO.output(input2,GPIO.HIGH)
        pwmA.ChangeDutyCycle(20)
    
    # Only left sensor detects black tape, turn left
    if (state_sensorLeft == True and state_sensorRight == False):
        GPIO.output(input4,GPIO.LOW)
        GPIO.output(input3,GPIO.HIGH)
        pwmB.ChangeDutyCycle(85)
        GPIO.output(input1,GPIO.LOW)
        GPIO.output(input2,GPIO.HIGH)
        pwmA.ChangeDutyCycle(20)
    
    # Neither sensor detects black tape, go straight
    else:
        GPIO.output(input3,GPIO.LOW)
        GPIO.output(input4,GPIO.LOW)
        pwmB.ChangeDutyCycle(0)
        GPIO.output(input1,GPIO.LOW)
        GPIO.output(input2,GPIO.HIGH)
        pwmA.ChangeDutyCycle(20)


