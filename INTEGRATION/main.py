#!/usr/bin/env python3

from vision import detectar_objeto_estable
from robot import portInit, nozzle_init, home, pick_up, ready, rutina_color

print("Sistema de Clasificación Iniciado")

portInit()
nozzle_init()

while True:
    print("Esperando detección estable...")
    home()
    resultado = detectar_objeto_estable(tiempo_objetivo=4)
    if resultado:
        color, forma = resultado
        print(f"Objeto detectado: {forma} de color {color}")
        pick_up()
        ready()
        rutina_color(color)
