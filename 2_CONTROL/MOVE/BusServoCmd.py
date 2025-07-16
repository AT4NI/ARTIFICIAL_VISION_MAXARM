#!/usr/bin/env python3
# encoding: utf-8
import time
import ctypes
import serial
import RPi.GPIO as GPIO

# Comandos para servo Hiwonder
LOBOT_SERVO_FRAME_HEADER = 0x55
LOBOT_SERVO_MOVE_TIME_WRITE = 1
LOBOT_SERVO_MOVE_STOP = 12

serialHandle = serial.Serial("/dev/ttyS0", 115200)  # UART0: TXD (GPIO14), RXD (GPIO15)

# Pines de control
rx_pin = 7   # GPIO4
tx_pin = 13  # GPIO27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def portInit():
    GPIO.setup(rx_pin, GPIO.OUT)
    GPIO.output(rx_pin, 0)
    GPIO.setup(tx_pin, GPIO.OUT)
    GPIO.output(tx_pin, 1)

def portWrite():
    GPIO.output(tx_pin, 1)
    GPIO.output(rx_pin, 0)

def portRead():
    GPIO.output(rx_pin, 1)
    GPIO.output(tx_pin, 0)

def checksum(buf):
    sum = 0x00
    for b in buf:
        sum += b
    sum = sum - 0x55 - 0x55
    return (~sum) & 0xff

def serial_servo_write_cmd(id, cmd, dat1=None, dat2=None):
    portWrite()
    buf = bytearray(b'\x55\x55')
    buf.append(id)
    if dat1 is None and dat2 is None:
        buf.append(3)
    elif dat2 is None:
        buf.append(4)
    else:
        buf.append(7)
    buf.append(cmd)
    if dat1 is not None and dat2 is None:
        buf.append(dat1 & 0xff)
    elif dat1 is not None and dat2 is not None:
        buf.extend([(dat1 & 0xff), (dat1 >> 8) & 0xff])
        buf.extend([(dat2 & 0xff), (dat2 >> 8) & 0xff])
    buf.append(checksum(buf))
    serialHandle.write(buf)

def move_servo(id, position, duration):
    serial_servo_write_cmd(id, LOBOT_SERVO_MOVE_TIME_WRITE, position, duration)

def stop_servo(id):
    serial_servo_write_cmd(id, LOBOT_SERVO_MOVE_STOP)
