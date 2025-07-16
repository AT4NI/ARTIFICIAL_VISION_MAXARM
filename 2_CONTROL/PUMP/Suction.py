import RPi.GPIO as GPIO
import time

# Pines según el código original en ESP32
PUMP_PIN1 = 21
PUMP_PIN2 = 19
VALVE_PIN1 = 18
VALVE_PIN2 = 5

def nozzle_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PUMP_PIN1, GPIO.OUT)
    GPIO.setup(PUMP_PIN2, GPIO.OUT)
    GPIO.setup(VALVE_PIN1, GPIO.OUT)
    GPIO.setup(VALVE_PIN2, GPIO.OUT)
    GPIO.output(PUMP_PIN1, GPIO.LOW)
    GPIO.output(PUMP_PIN2, GPIO.LOW)
    GPIO.output(VALVE_PIN1, GPIO.LOW)
    GPIO.output(VALVE_PIN2, GPIO.LOW)

def pump_on():
    GPIO.output(PUMP_PIN1, GPIO.LOW)
    GPIO.output(PUMP_PIN2, GPIO.HIGH)

def valve_on():
    GPIO.output(PUMP_PIN1, GPIO.LOW)
    GPIO.output(PUMP_PIN2, GPIO.LOW)
    GPIO.output(VALVE_PIN1, GPIO.LOW)
    GPIO.output(VALVE_PIN2, GPIO.HIGH)

def valve_off():
    GPIO.output(VALVE_PIN1, GPIO.LOW)
    GPIO.output(VALVE_PIN2, GPIO.LOW)
