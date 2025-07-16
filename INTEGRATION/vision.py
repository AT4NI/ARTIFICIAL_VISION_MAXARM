import cv2
import numpy as np
import time

# Rangos HSV calibrados
rangos_hsv = {
    "Azul": ([96, 201, 178], [179, 255, 255]),
    "Verde": ([64, 180, 167], [99, 255, 248]),
    "Rojo": ([131, 38, 171], [179, 194, 255]),
    "Amarillo": ([66, 28, 226], [87, 77, 255]),
    "Naranja": ([3, 0, 203], [50, 110, 255]),
    "Carne": ([87, 29, 229], [99, 77, 255]),
}

def detectar_objeto_estable(tiempo_objetivo=4):
    cap = cv2.VideoCapture(0)
    anterior = None
    tiempo_inicio = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (320, 240))
        original = frame.copy()
        resultado = frame.copy()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        detectado = None

        for color, (bajo, alto) in rangos_hsv.items():
            mascara = cv2.inRange(hsv, np.array(bajo), np.array(alto))
            mascara = cv2.GaussianBlur(mascara, (3, 3), 1.2)
            mascara = cv2.medianBlur(mascara, 3)

            contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contornos:
                area = cv2.contourArea(cnt)
                if area > 1000:
                    perimetro = cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, 0.03 * perimetro, True)
                    forma = detectar_forma(approx, area, perimetro)
                    if forma != "Desconocido":
                        detectado = (color, forma)
                        break
            if detectado:
                break

        if detectado == anterior:
            if tiempo_inicio is None:
                tiempo_inicio = time.time()
            elif time.time() - tiempo_inicio >= tiempo_objetivo:
                cap.release()
                cv2.destroyAllWindows()
                return detectado
        else:
            anterior = detectado
            tiempo_inicio = None

        cv2.imshow("Original", original)
        cv2.imshow("Resultado", resultado)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

# Reutilizamos tu función de detectar_forma
def calcular_angulos(puntos):
    def angulo(p1, p2, p3):
        v1 = p1 - p2
        v2 = p3 - p2
        cos_ang = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.degrees(np.arccos(np.clip(cos_ang, -1.0, 1.0)))
    return [angulo(puntos[i - 1][0], puntos[i][0], puntos[(i + 1) % len(puntos)][0]) for i in range(len(puntos))]

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
        angs = calcular_angulos(approx.reshape((-1, 1, 2)))
        pendientes = [pendiente(pts[i], pts[(i + 1) % 4]) for i in range(4)]
        paralelos = 0
        if abs(pendientes[0] - pendientes[2]) < 0.35: paralelos += 1
        if abs(pendientes[1] - pendientes[3]) < 0.35: paralelos += 1
        angulos_rectos = all(83 <= a <= 97 for a in angs)
        lados_iguales = max(lados) - min(lados) < 10
        if angulos_rectos and paralelos == 2:
            return "Rectángulo"
        if paralelos == 1 and angulos_rectos:
            return "Rectángulo"
        if lados_iguales:
            min_ang = min(angs)
            max_ang = max(angs)
            if 55 <= min_ang <= 65 and 115 <= max_ang <= 125:
                return "Rombo 1"
            elif 25 <= min_ang <= 35 and 145 <= max_ang <= 155:
                return "Rombo 2"
            else:
                return "Rombo"
        return "Trapecio"
    elif vertices == 6:
        return "Hexágono"
    return "Desconocido"
