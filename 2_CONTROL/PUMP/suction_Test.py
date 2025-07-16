import time
import suction_nozzle

suction_nozzle.nozzle_init()

print("Inicio...")

# Una sola secuencia como en el .ino
suction_nozzle.pump_on()
time.sleep(2)

suction_nozzle.valve_on()
time.sleep(0.5)

suction_nozzle.valve_off()
time.sleep(2)

print("Finalizado.")
