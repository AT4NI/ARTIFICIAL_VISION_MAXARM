#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from BusServoCmd import move_servo, portInit

# Inicializar puerto UART
portInit()

# Crear ventana principal
root = tk.Tk()
root.title("Panel de Control de Servos Hiwonder HTS-35H")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Título principal
main_label = ttk.Label(root, text="Control de 3 Servos - HTS-35H", font=("Arial", 16, "bold"))
main_label.pack(pady=10)

# Diccionario para guardar etiquetas de posición
position_labels = {}

# Función para mover servo y actualizar etiqueta
def update_servo(id, value):
    pos = int(float(value))
    move_servo(id, pos, 1500)
    position_labels[id].config(text=f"Posición: {pos}")

# Crear sección para cada servo
for i in range(1, 4):  # Servo IDs 1, 2, 3
    frame = ttk.LabelFrame(root, text=f"Servo ID {i}", padding=15)
    frame.pack(fill='x', padx=20, pady=10)

    # Slider
    slider = ttk.Scale(
        frame,
        from_=0,
        to=1000,
        orient="horizontal",
        length=350,
        command=lambda val, sid=i: update_servo(sid, val)
    )
    slider.set(400)
    slider.pack()

    # Etiqueta de posición
    lbl = ttk.Label(frame, text="Posición: 400", font=("Arial", 11))
    lbl.pack(pady=5)
    position_labels[i] = lbl

# Ejecutar interfaz
root.mainloop()
