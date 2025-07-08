import cv2

# Crear ventanas una vez
cv2.namedWindow("Original")
cv2.namedWindow("Filtro Gaussiano")
cv2.namedWindow("Filtro de Mediana")
cv2.namedWindow("Filtro Combinado")

# Inicializar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar para eficiencia si es necesario (opcional)
    frame = cv2.resize(frame, (320, 240))

    # Aplicar filtro Gaussiano
    gauss = cv2.GaussianBlur(frame, (3, 3), 1.4)

    # Aplicar filtro de Mediana
    mediana = cv2.medianBlur(frame, 3)

    # Aplicar filtro combinado (Primero Gaussiano, luego Mediana)
    combinado = cv2.medianBlur(gauss, 5)

    # Mostrar ventanas
    cv2.imshow("Original", frame)
    cv2.imshow("Filtro Gaussiano", gauss)
    cv2.imshow("Filtro de Mediana", mediana)
    cv2.imshow("Filtro Combinado", combinado)

    # Salir con tecla ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
