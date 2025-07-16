#!/usr/bin/env python3
import time
from BusServoCmd import portInit, move_servo
import Suction
import RPi.GPIO as GPIO
import time

print("RUTINA TEST")
portInit()
Suction.nozzle_init()
while True:
# HOME
    print("HOME")
    move_servo(1, 723, 1500)  # S1
    time.sleep(2)
    move_servo(3, 556, 1500)  # S3
    time.sleep(2)
    move_servo(2, 540, 1200)    # S2
    time.sleep(2)
# PICK UP
    print("PICK")
    move_servo(1, 864, 1500)  # S1 - PRINCIPAL
    time.sleep(2)
    move_servo(3, 600, 1500)  # S3 - INTER INICIO
    time.sleep(2)
    move_servo(2, 400, 1200)  # S2
    time.sleep(2)
    move_servo(3, 761, 1500)  # S3 - FINAL INICIO
    time.sleep(2)
    Suction.pick()
    move_servo(2, 286, 1200)  # S2
    time.sleep(2)
    move_servo(2, 400, 1200)  # S2
    time.sleep(2) 
    move_servo(3, 600, 1500)  # S3 - INTER FINAL
    time.sleep(2)
   
# READY
    print("READY")
    move_servo(1, 864, 1500)  # S1
    time.sleep(2)
    move_servo(3, 590, 1500)  # S3
    time.sleep(2)
    move_servo(2, 628, 1200)    # S2
    time.sleep(2)
    move_servo(3, 544, 1500)  # S3
    time.sleep(2)     
 # CARNE
    print("CARNE")
    move_servo(1, 590, 1500)  # S1
    time.sleep(2)
    move_servo(2, 500, 1200)    # S2
    time.sleep(2) 
    move_servo(3, 700, 1500)  # S3
    time.sleep(2)
    move_servo(2, 430, 1200)    # S2
    time.sleep(2)
    move_servo(3, 745, 1500)  # S3
    time.sleep(2)
    move_servo(2, 430, 1200)    # S2
    time.sleep(2)
    move_servo(3, 700, 1500)  # S3
    time.sleep(2)    
    move_servo(2, 500, 1200)    # S2
    time.sleep(2)
    move_servo(3, 544, 1500)  # S3
    time.sleep(2) 
    move_servo(2, 628, 1200)    # S2
    time.sleep(2)
 # HOME
    print("HOME")
    move_servo(1, 723, 1500)  # S1
    time.sleep(2)
    move_servo(3, 556, 1500)  # S3
    time.sleep(2)
    move_servo(2, 540, 1200)    # S2
    time.sleep(2)   
 # VERDE
    print("VERDE")
    move_servo(1, 590, 1500)  # S1
    time.sleep(2)
    move_servo(3, 580, 1500)  # S3
    time.sleep(2)
    move_servo(2, 380, 1200)    # S2
    time.sleep(2) 
    move_servo(3, 628, 1500)  # S3
    time.sleep(2)
    move_servo(2, 248, 1200)    # S2
    time.sleep(2) 
    move_servo(2, 380, 1200)    # S2
    time.sleep(2)  
    move_servo(3, 544, 1500)  # S3
    time.sleep(2)
    move_servo(2, 628, 1200)    # S2
    time.sleep(2)  
 # HOME
    print("HOME")
    move_servo(1, 723, 1500)  # S1
    time.sleep(2)
    move_servo(3, 556, 1500)  # S3
    time.sleep(2)
    move_servo(2, 540, 1200)    # S2
    time.sleep(2)     
 # NARANJA
    print("NARANJA")
    move_servo(1, 380, 1500)  # S1
    time.sleep(2)
    move_servo(2, 500, 1200)    # S2
    time.sleep(2) 
    move_servo(3, 700, 1500)  # S3
    time.sleep(2)
    move_servo(2, 430, 1200)    # S2
    time.sleep(2)
    move_servo(3, 745, 1500)  # S3
    time.sleep(2)
    move_servo(2, 430, 1200)    # S2
    time.sleep(2)
    move_servo(3, 700, 1500)  # S3
    time.sleep(2)    
    move_servo(2, 500, 1200)    # S2
    time.sleep(2)
    move_servo(3, 544, 1500)  # S3
    time.sleep(2) 
    move_servo(2, 628, 1200)    # S2
    time.sleep(2)   
 # HOME
    print("HOME")
    move_servo(1, 723, 1500)  # S1
    time.sleep(2)
    move_servo(3, 556, 1500)  # S3
    time.sleep(2)
    move_servo(2, 540, 1200)    # S2
    time.sleep(2)
 # AZUL
    print("AZUL")
    move_servo(1, 380, 1500)  # S1
    time.sleep(2)
    move_servo(3, 580, 1500)  # S3
    time.sleep(2)
    move_servo(2, 380, 1200)    # S2
    time.sleep(2) 
    move_servo(3, 628, 1500)  # S3
    time.sleep(2)
    move_servo(2, 248, 1200)    # S2
    time.sleep(2) 
    move_servo(2, 380, 1200)    # S2
    time.sleep(2)  
    move_servo(3, 544, 1500)  # S3
    time.sleep(2)
    move_servo(2, 628, 1200)    # S2
    time.sleep(2)   
 # HOME
    print("HOME")
    move_servo(1, 723, 1500)  # S1
    time.sleep(2)
    move_servo(3, 556, 1500)  # S3
    time.sleep(2)
    move_servo(2, 540, 1200)    # S2
    time.sleep(2)     
 # ROJO
    print("ROJO")
    move_servo(1, 170, 1500)  # S1
    time.sleep(2)
    move_servo(2, 500, 1200)    # S2
    time.sleep(2) 
    move_servo(3, 700, 1500)  # S3
    time.sleep(2)
    move_servo(2, 430, 1200)    # S2
    time.sleep(2)
    move_servo(3, 745, 1500)  # S3
    time.sleep(2)
    move_servo(2, 430, 1200)    # S2
    time.sleep(2)
    move_servo(3, 700, 1500)  # S3
    time.sleep(2)    
    move_servo(2, 500, 1200)    # S2
    time.sleep(2)
    move_servo(3, 544, 1500)  # S3
    time.sleep(2) 
    move_servo(2, 628, 1200)    # S2
    time.sleep(2)  
 # HOME
    print("HOME")
    move_servo(1, 723, 1500)  # S1
    time.sleep(2)
    move_servo(3, 556, 1500)  # S3
    time.sleep(2)
    move_servo(2, 540, 1200)    # S2
    time.sleep(2)
 # AMARILLO
    print("AMARILLO")
    move_servo(1, 170, 1500)  # S1
    time.sleep(2)
    move_servo(3, 580, 1500)  # S3
    time.sleep(2)
    move_servo(2, 380, 1200)    # S2
    time.sleep(2) 
    move_servo(3, 628, 1500)  # S3
    time.sleep(2)
    move_servo(2, 248, 1200)    # S2
    time.sleep(2) 
    move_servo(2, 380, 1200)    # S2
    time.sleep(2)  
    move_servo(3, 544, 1500)  # S3
    time.sleep(2)
    move_servo(2, 628, 1200)    # S2
    time.sleep(2)   
 # HOME
    print("HOME")
    move_servo(1, 723, 1500)  # S1
    time.sleep(2)
    move_servo(3, 556, 1500)  # S3
    time.sleep(2)
    move_servo(2, 540, 1200)    # S2
    time.sleep(2) 


