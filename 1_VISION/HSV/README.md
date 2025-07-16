## Detección de Colores con Filtros HSV

### Concepto

El modelo de color **HSV (Hue, Saturation, Value)** es una representación más intuitiva para segmentación de colores que el modelo RGB. Separar el tono (**Hue**) de la intensidad (**Value**) y saturación (**Saturation**) permite detectar colores de manera más robusta, incluso en condiciones de iluminación variables. Este sistema es ampliamente utilizado en visión por computadora y robótica.

En este proyecto, se implementa un sistema de calibración interactivo basado en HSV para ajustar en tiempo real los rangos de detección de colores. Este es un paso fundamental para una correcta clasificación de objetos por color usando una cámara.

---

### Descripción detallada del código

```python
import cv2
import numpy as np
```
**Importación de librerías necesarias:** OpenCV para visión artificial y NumPy para manejo de matrices.

```python
def empty(a):
    pass
```
**Función vacía:** requerida por `createTrackbar` como callback, aunque no realiza ninguna acción.

```python
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
```
**Ventana de sliders:** se crea y se ajusta el tamaño para una mejor interfaz.

```python
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
```
**Sliders para rango HSV:** permiten ajustar los valores mínimos y máximos de cada componente del modelo HSV.

```python
cv2.namedWindow("Original | Detección HSV con filtro")
```
**Ventana principal:** única ventana donde se mostrará la imagen original y la imagen segmentada.

```python
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()
print("Cámara iniciada con filtros. Ajusta sliders. Presiona 's' para salir.")
```
**Inicialización de cámara:** se abre la cámara y se verifica que funcione correctamente. Se muestra mensaje de bienvenida.

```python
while True:
    ret, img = cap.read()
    if not ret:
        print("No se pudo capturar imagen.")
        break
```
**Captura continua:** bucle principal que obtiene imagen de la cámara. Se rompe si hay error.

```python
    img = cv2.resize(img, (320, 240))
```
**Reducción de resolución:** para mejorar rendimiento.

```python
    filtrada = cv2.GaussianBlur(img, (3, 3), 1.4)
    filtrada = cv2.medianBlur(filtrada, 3)
```
**Filtros:** Gaussiano y Mediana para eliminar ruido y suavizar la imagen.

```python
    imgHSV = cv2.cvtColor(filtrada, cv2.COLOR_BGR2HSV)
```
**Conversión a HSV:** paso esencial para trabajar en el espacio de color adecuado.

```python
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
```
**Lectura de sliders:** se obtienen los valores actuales definidos por el usuario.

```python
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
```
**Creación de máscara:** identifica los píxeles dentro del rango seleccionado.

```python
    imgResult = cv2.bitwise_and(img, img, mask=mask)
```
**Aplicación de máscara:** mantiene solo las zonas que cumplen con el color detectado.

```python
    imgStack = np.hstack([img, imgResult])
    cv2.imshow("Original | Detección HSV con filtro", imgStack)
```
**Visualización:** se apilan horizontalmente la imagen original y la procesada.

```python
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Finalizando.")
        break
```
**Salida del bucle:** se termina si el usuario presiona la tecla `'s'`.

```python
cap.release()
cv2.destroyAllWindows()
```
**Limpieza final:** se liberan los recursos usados por la cámara y se cierran las ventanas.
