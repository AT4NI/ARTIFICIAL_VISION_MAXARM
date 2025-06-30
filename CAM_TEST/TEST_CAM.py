import cv2

# Abrir la cámara conectada en /dev/video0
cap = cv2.VideoCapture(0)

# Verificar si se abrió correctamente
if not cap.isOpened():
    print("❌ No se pudo abrir la cámara.")
    exit()

print("✅ Cámara abierta correctamente. Presiona 's' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No se pudo leer imagen.")
        break

    # Mostrar el frame en una ventana
    cv2.imshow("Vista en vivo", frame)

    # Salir al presionar la tecla 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()