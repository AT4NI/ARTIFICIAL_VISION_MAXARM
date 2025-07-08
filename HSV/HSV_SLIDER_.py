import cv2
import numpy as np

def empty(a):
    pass

# Crear ventana con sliders para HSV
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# Crear ventana de visualización UNA sola vez
cv2.namedWindow("Original | Detección HSV con filtro")

# Iniciar cámara
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()
print("Cámara iniciada con filtros. Ajusta sliders. Presiona 's' para salir.")

while True:
    ret, img = cap.read()
    if not ret:
        print("No se pudo capturar imagen.")
        break

    img = cv2.resize(img, (320, 240))

    # 🧼 Filtro Gaussiano + Mediana
    filtrada = cv2.GaussianBlur(img, (3, 3), 1.4)
    filtrada = cv2.medianBlur(filtrada, 3)

    # 🎨 Convertir a HSV
    imgHSV = cv2.cvtColor(filtrada, cv2.COLOR_BGR2HSV)

    # 📊 Leer sliders
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # 🧪 Crear máscara y aplicar
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # 📺 Mostrar en ventana ya creada
    imgStack = np.hstack([img, imgResult])
    cv2.imshow("Original | Detección HSV con filtro", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Finalizando.")
        break

cap.release()
cv2.destroyAllWindows()
