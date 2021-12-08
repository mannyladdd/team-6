import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

motionSensorPin = 11
ledPin = 3, 7, 19
GPIO.setup(motionSensorPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

ledState = False
detectMotion = 0
polltime = 0.2

def toggleLight(ledState, ledPin):
    ledState = not ledState
    GPIO.output(ledPin, ledState)
    return ledState

while True:
    input = GPIO.input(motionSensorPin)

    if input == 0:
        print("Nothing Detected", input, ledState)
        detectMotion = 0
    elif input == 1:
        print("Motion Detected", input, ledState)
        if not detectMotion:
            ledState = toggleLight(ledState, ledPin)
            print(f"LED toggled {ledState}.")
            detectMotion = 1
    
    time.sleep(polltime)