## Concepto

### HSV

Las siglas significan: Hue (tono), Saturation (saturación), Value (valor o brillo). Es un \*\*modelo de color para procesamiento de imágenes\*\*, porque separa la información del color (tono) de la intensidad (saturación y brillo).



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

rojo\_bajo1 = np.array(\[0, 150, 100])

rojo\_alto1 = np.array(\[10, 255, 255])

rojo\_bajo2 = np.array(\[160, 150, 100])

rojo\_alto2 = np.array(\[179, 255, 255])

azul\_bajo = np.array(\[100, 150, 100])

azul\_alto = np.array(\[125, 255, 255])

amarillo\_bajo = np.array(\[20, 150, 100])

amarillo\_alto = np.array(\[40, 255, 255])

```
- Cada color está definido por un rango en HSV.
- El rojo se detecta en dos rangos porque el tono rojo está al inicio y al final del espectro hue (0-10 y 160-179).
- Cada `np.array` es `\[Hue, Saturación, Valor]` mínimos o máximos.
- Estos valores son calibrados previamente y definen qué píxeles serán considerados del color respectivo.

### Diferenciar Formas
```py

def calcular\_angulos(puntos):

&nbsp;   def angulo(p1, p2, p3):

&nbsp;       v1 = p1 - p2

&nbsp;       v2 = p3 - p2

&nbsp;       cos\_ang = np.dot(v1, v2) / (np.linalg.norm(v1) \* np.linalg.norm(v2))

&nbsp;       return np.degrees(np.arccos(np.clip(cos\_ang, -1.0, 1.0)))

&nbsp;   

&nbsp;   angs = \[]

&nbsp;   for i in range(len(puntos)):

&nbsp;       p1 = puntos\[i - 1]\[0]

&nbsp;       p2 = puntos\[i]\[0]

&nbsp;       p3 = puntos\[(i + 1) % len(puntos)]\[0]

&nbsp;       angs.append(angulo(p1, p2, p3))

&nbsp;   return angs

```
- Calcula los ángulos internos de una figura dado un conjunto de puntos (vértices).
- Esto es útil para diferenciar rectángulos (ángulos ~90°), trapecios, rombos, etc.

###  Pendiente entre dos puntos
```py

def pendiente(p1, p2):

&nbsp;   if p2\[0] - p1\[0] == 0:

&nbsp;       return float('inf')

&nbsp;   return (p2\[1] - p1\[1]) / (p2\[0] - p1\[0])

```
- Calcula la pendiente entre dos puntos (x,y).
- Se usa para verificar paralelismo de lados (por ejemplo, para trapecios o rombos).

### Deteccion (Vértices y Propiedades Geométricas)
```py

def detectar\_forma(approx, area, perimetro):

&nbsp;   vertices = len(approx)

&nbsp;   approx = approx.reshape((vertices, 2))



&nbsp;   if vertices == 3:

&nbsp;       return "Triángulo"



&nbsp;   elif vertices == 4:

&nbsp;       pts = approx

&nbsp;       lados = \[np.linalg.norm(pts\[i] - pts\[(i + 1) % 4]) for i in range(4)]

&nbsp;       lados\_iguales = max(lados) - min(lados) < 10

&nbsp;       angs = calcular\_angulos(approx.reshape((-1, 1, 2)))

&nbsp;       angulos\_rectos = all(85 <= a <= 95 for a in angs)

&nbsp;       pendientes = \[pendiente(pts\[i], pts\[(i + 1) % 4]) for i in range(4)]

&nbsp;       paralelos = 0

&nbsp;       if abs(pendientes\[0] - pendientes\[2]) < 0.2: paralelos += 1

&nbsp;       if abs(pendientes\[1] - pendientes\[3]) < 0.2: paralelos += 1



&nbsp;       if angulos\_rectos and paralelos == 2:

&nbsp;           return "Rectángulo"

&nbsp;       elif lados\_iguales and not angulos\_rectos:

&nbsp;           return "Rombo"

&nbsp;       elif paralelos == 1:

&nbsp;           return "Trapecio"



&nbsp;   elif vertices == 6:

&nbsp;       return "Hexágono"



&nbsp;   elif vertices > 6:

&nbsp;       circularidad = 4 \* np.pi \* area / (perimetro \* perimetro)

&nbsp;       if circularidad > 0.8:

&nbsp;           return "Círculo"



&nbsp;   return "Desconocido"

```



- La función usa el número de vértices aproximados para empezar a clasificar la forma.
- Si es triángulo, retorna "Triángulo".
- Para 4 vértices, se usa el análisis de lados, ángulos y paralelismo para diferenciar entre rectángulo, rombo o trapecio.
- Si tiene 6 vértices, se considera hexágono.
- Más de 6 y con alta circularidad se considera círculo.
- Retorna "Desconocido" si no encaja en ninguna.



