import cv2
import numpy as np

# ------- Valores HSV calibrados para colores -------
rojo_bajo1 = np.array([0, 150, 100])
rojo_alto1 = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 150, 100])
rojo_alto2 = np.array([179, 255, 255])

azul_bajo = np.array([100, 150, 100])
azul_alto = np.array([125, 255, 255])

amarillo_bajo = np.array([20, 150, 100])
amarillo_alto = np.array([40, 255, 255])

# ------- Funciones para detectar forma y color -------

def calcular_angulos(puntos):
    def angulo(p1, p2, p3):
        v1 = p1 - p2
        v2 = p3 - p2
        cos_ang = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(np.clip(cos_ang, -1.0, 1.0)))
    
    angs = []
    for i in range(len(puntos)):
        p1 = puntos[i - 1][0]
        p2 = puntos[i][0]
        p3 = puntos[(i + 1) % len(puntos)][0]
        angs.append(angulo(p1, p2, p3))
    return angs

def pendiente(p1, p2):
    if p2[0] - p1[0] == 0:
        return float('inf')
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def detectar_forma(approx, area, perimetro):
    vertices = len(approx)
    approx = approx.reshape((vertices, 2))

    if vertices == 3:
        return "Triángulo"

    elif vertices == 4:
        pts = approx
        lados = [np.linalg.norm(pts[i] - pts[(i + 1) % 4]) for i in range(4)]
        lados_iguales = max(lados) - min(lados) < 10
        angs = calcular_angulos(approx.reshape((-1, 1, 2)))
        angulos_rectos = all(85 <= a <= 95 for a in angs)
        pendientes = [pendiente(pts[i], pts[(i + 1) % 4]) for i in range(4)]
        paralelos = 0
        if abs(pendientes[0] - pendientes[2]) < 0.2: paralelos += 1
        if abs(pendientes[1] - pendientes[3]) < 0.2: paralelos += 1

        if angulos_rectos and paralelos == 2:
            return "Rectángulo"
        elif lados_iguales and not angulos_rectos:
            return "Rombo"
        elif paralelos == 1:
            return "Trapecio"

    elif vertices == 6:
        return "Hexágono"

    elif vertices > 6:
        circularidad = 4 * np.pi * area / (perimetro * perimetro)
        if circularidad > 0.8:
            return "Círculo"

    return "Desconocido"

def detectar_color(hsv, contorno):
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contorno], -1, 255, -1)
    mean = cv2.mean(hsv, mask=mask)
    h, s, v = mean[:3]

    # Comprobar rojo (dos rangos)
    if ((rojo_bajo1[0] <= h <= rojo_alto1[0]) or (rojo_bajo2[0] <= h <= rojo_alto2[0])) and s >= 150 and v >= 100:
        return "Rojo"
    elif azul_bajo[0] <= h <= azul_alto[0] and s >= 150 and v >= 100:
        return "Azul"
    elif amarillo_bajo[0] <= h <= amarillo_alto[0] and s >= 150 and v >= 100:
        return "Amarillo"
    else:
        return "Otro"

# ------- Inicialización cámara y ventana única -------

cv2.namedWindow("Camara", cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

print("Cámara abierta correctamente. Presiona 's' para salir.")

# ------- Bucle principal -------

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer imagen.")
        break

    frame = cv2.resize(frame, (320, 240))
    img_blur = cv2.GaussianBlur(frame, (5, 5), 1)
    img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(img_gray, 50, 150)

    contornos, _ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > 1000:
            perimetro = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimetro, True)

            forma = detectar_forma(approx, area, perimetro)
            color = detectar_color(img_hsv, cnt)

            if forma != "Desconocido" and color != "Otro":
                x, y, w, h = cv2.boundingRect(approx)
                etiqueta = f"{forma} {color}"

                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
                cv2.putText(frame, etiqueta, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Finalizando...")
        break

cap.release()
cv2.destroyAllWindows()
