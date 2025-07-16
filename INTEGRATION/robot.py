# robot.py
import time
from BusServoCmd import move_servo, portInit
from Suction import nozzle_init, pick, place, pump_off

def home():
    move_servo(1, 723, 1500); time.sleep(2)
    move_servo(3, 556, 1500); time.sleep(2)
    move_servo(2, 540, 1200); time.sleep(2)

def pick_up():
    move_servo(1, 864, 1500); time.sleep(2)
    move_servo(3, 600, 1500); time.sleep(2)
    move_servo(2, 400, 1200); time.sleep(2)
    move_servo(3, 761, 1500); time.sleep(2)
    move_servo(2, 286, 1200); time.sleep(2)
    pick()
    move_servo(2, 400, 1200); time.sleep(2)
    move_servo(3, 600, 1500); time.sleep(2)

def ready():
    move_servo(1, 864, 1500); time.sleep(2)
    move_servo(3, 590, 1500); time.sleep(2)
    move_servo(2, 628, 1200); time.sleep(2)
    move_servo(3, 544, 1500); time.sleep(2)

def rutina_color(color):
    if color == "Carne":
        move_servo(1, 590, 1500); time.sleep(2)
        move_servo(2, 500, 1200); time.sleep(2)
        move_servo(3, 700, 1500); time.sleep(2)
        move_servo(2, 430, 1200); time.sleep(2)
        move_servo(3, 745, 1500); time.sleep(2)
        pump_off()
        move_servo(2, 430, 1200); time.sleep(2)
        move_servo(3, 700, 1500); time.sleep(2)
        move_servo(2, 500, 1200); time.sleep(2)
        place()
        move_servo(3, 544, 1500); time.sleep(2)
        move_servo(2, 628, 1200); time.sleep(2)

    elif color == "Verde":
        move_servo(1, 590, 1500); time.sleep(2)
        move_servo(3, 580, 1500); time.sleep(2)
        move_servo(2, 380, 1200); time.sleep(2)
        pump_off()
        move_servo(3, 628, 1500); time.sleep(2)
        move_servo(2, 248, 1200); time.sleep(2)
        place()
        move_servo(2, 380, 1200); time.sleep(2)
        move_servo(3, 544, 1500); time.sleep(2)
        move_servo(2, 628, 1200); time.sleep(2)

    elif color == "Naranja":
        move_servo(1, 380, 1500); time.sleep(2)
        move_servo(2, 500, 1200); time.sleep(2)
        move_servo(3, 700, 1500); time.sleep(2)
        move_servo(2, 430, 1200); time.sleep(2)
        move_servo(3, 745, 1500); time.sleep(2)
        pump_off()
        move_servo(2, 430, 1200); time.sleep(2)
        move_servo(3, 700, 1500); time.sleep(2)
        move_servo(2, 500, 1200); time.sleep(2)
        place()
        move_servo(3, 544, 1500); time.sleep(2)
        move_servo(2, 628, 1200); time.sleep(2)

    elif color == "Azul":
        move_servo(1, 380, 1500); time.sleep(2)
        move_servo(3, 580, 1500); time.sleep(2)
        move_servo(2, 380, 1200); time.sleep(2)
        pump_off()
        move_servo(3, 628, 1500); time.sleep(2)
        move_servo(2, 248, 1200); time.sleep(2)
        place()
        move_servo(2, 380, 1200); time.sleep(2)
        move_servo(3, 544, 1500); time.sleep(2)
        move_servo(2, 628, 1200); time.sleep(2)

    elif color == "Rojo":
        move_servo(1, 170, 1500); time.sleep(2)
        move_servo(2, 500, 1200); time.sleep(2)
        move_servo(3, 700, 1500); time.sleep(2)
        move_servo(2, 430, 1200); time.sleep(2)
        move_servo(3, 745, 1500); time.sleep(2)
        pump_off()
        move_servo(2, 430, 1200); time.sleep(2)
        move_servo(3, 700, 1500); time.sleep(2)
        move_servo(2, 500, 1200); time.sleep(2)
        place()
        move_servo(3, 544, 1500); time.sleep(2)
        move_servo(2, 628, 1200); time.sleep(2)

    elif color == "Amarillo":
        move_servo(1, 170, 1500); time.sleep(2)
        move_servo(3, 580, 1500); time.sleep(2)
        move_servo(2, 380, 1200); time.sleep(2)
        pump_off()
        move_servo(3, 628, 1500); time.sleep(2)
        move_servo(2, 248, 1200); time.sleep(2)
        place()
        move_servo(2, 380, 1200); time.sleep(2)
        move_servo(3, 544, 1500); time.sleep(2)
        move_servo(2, 628, 1200); time.sleep(2)

    else:
        print(f"Color '{color}' no reconocido. No se ejecutó ninguna rutina.")
