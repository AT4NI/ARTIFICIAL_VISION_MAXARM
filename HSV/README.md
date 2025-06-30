## Concepto
### HSV
Las siglas significan: Hue (tono), Saturation (saturación), Value (valor o brillo). Es un **modelo de color para procesamiento de imágenes**, porque separa la información del color (tono) de la intensidad (saturación y brillo).

- Hue (tono): representa el color, se mide en grados (0 a 179 en OpenCV, donde 0° es rojo, ~60° es amarillo, ~120° es verde, ~180° es azul, etc.).
- Saturation (saturación): qué tan puro es el color (0 a 255). Un valor bajo indica un color grisáceo, uno alto es color intenso.
- Value (valor o brillo): qué tan claro u oscuro es el color (0 a 255). 0 es negro, 255 es brillo máximo.

Usamos HSV porque es más robusto para detectar colores que el modelo RGB/BGR clásico, que es sensible a cambios de luz.
## Código
En la siguiente sección se dara una explicación sobre el código desarrollado para el desglose de HSV en 3 pantallas (Original, B/N y Color).
### Librerías
```py
import cv2
import numpy as np
```
- `cv2` es OpenCV, librería para visión artificial.
- `numpy` es para manipular arreglos, vectores y matrices.

### Rangos HSV por color
```py
rojo_bajo1 = np.array([0, 150, 100])
rojo_alto1 = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 150, 100])
rojo_alto2 = np.array([179, 255, 255])
azul_bajo = np.array([100, 150, 100])
azul_alto = np.array([125, 255, 255])
amarillo_bajo = np.array([20, 150, 100])
amarillo_alto = np.array([40, 255, 255])
```

- Cada color está definido por un rango en HSV.

- El rojo se detecta en dos rangos porque el tono rojo está al inicio y al final del espectro hue (0-10 y 160-179).

- Cada `np.array` es `[Hue, Saturación, Valor]` mínimos o máximos.

- Estos valores son calibrados previamente y definen qué píxeles serán considerados del color respectivo.

### Diferenciar Formas
```py
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
```
- Calcula los ángulos internos de una figura dado un conjunto de puntos (vértices).
- Esto es útil para diferenciar rectángulos (ángulos ~90°), trapecios, rombos, etc.

###  Pendiente entre dos puntos

```py
def pendiente(p1, p2):
    if p2[0] - p1[0] == 0:
        return float('inf')
    return (p2[1] - p1[1]) / (p2[0] - p1[0])
```

- Calcula la pendiente entre dos puntos (x,y).
- Se usa para verificar paralelismo de lados (por ejemplo, para trapecios o rombos).

### Deteccion (Vértices y Propiedades Geométricas)
```py
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
```

- La función usa el número de vértices aproximados para empezar a clasificar la forma.
- Si es triángulo, retorna "Triángulo".
- Para 4 vértices, se usa el análisis de lados, ángulos y paralelismo para diferenciar entre rectángulo, rombo o trapecio.
- Si tiene 6 vértices, se considera hexágono.
- Más de 6 y con alta circularidad se considera círculo.
- Retorna "Desconocido" si no encaja en ninguna.

### Color Predominante
```py
def detectar_color(hsv, contorno):
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contorno], -1, 255, -1)  # Rellenar el contorno en máscara
    mean = cv2.mean(hsv, mask=mask)  # Media HSV dentro del contorno
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
```
- Crea una máscara solo del contorno.
- Calcula la media de HSV en esa zona.
- Determina el color comparando con los rangos HSV calibrados.
- Si no está dentro de los rangos, retorna "Otro".

### Inicialización de la cámara y ventana
```py
cv2.namedWindow("Camara", cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

print("Cámara abierta correctamente. Presiona 's' para salir.")
```
- Se crea una ventana con nombre fija para evitar múltiples ventanas.
- Se abre la cámara (índice 0).
- Se verifica que la cámara esté lista.

## Bucle Principal (Captura y Procesamiento)
```py
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer imagen.")
        break

    # Reducimos tamaño para mejor rendimiento
    frame = cv2.resize(frame, (320, 240))

    # Aplicamos desenfoque para reducir ruido
    img_blur = cv2.GaussianBlur(frame, (5, 5), 1)

    # Convertimos a HSV para detección de color
    img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

    # Convertimos a gris para detectar bordes
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    # Detectamos bordes con Canny
    img_canny = cv2.Canny(img_gray, 50, 150)

    # Encontramos contornos
    contornos, _ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > 1000:  # Filtrar áreas pequeñas/no relevantes
            perimetro = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimetro, True)

            # Detectar forma y color
            forma = detectar_forma(approx, area, perimetro)
            color = detectar_color(img_hsv, cnt)

            if forma != "Desconocido" and color != "Otro":
                x, y, w, h = cv2.boundingRect(approx)
                etiqueta = f"{forma} {color}"

                # Dibujar contorno y etiquetas en la imagen
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
                cv2.putText(frame, etiqueta, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

    # Mostrar el resultado final
    cv2.imshow("Camara", frame)

    # Salir si presionas 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Finalizando...")
        break

cap.release()
cv2.destroyAllWindows()
```
- Capturamos cada frame, filtramos, detectamos bordes y contornos.
- Para cada contorno significativo, detectamos la forma y el color.
- Si ambos son válidos, dibujamos la figura y escribimos el texto con forma y color.
- Solo hay una ventana que se actualiza, evitando el problema de ventanas múltiples.
- Se sale con la tecla 's'.

