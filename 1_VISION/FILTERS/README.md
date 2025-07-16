## Preprocesamiento de Imágenes: Filtros Gaussiano y de Mediana

### Preprocesamiento

El **preprocesamiento** en visión artificial es una etapa fundamental para preparar las imágenes antes de su análisis o reconocimiento. Su objetivo principal es mejorar la calidad de la imagen, reducir el ruido y destacar características importantes, facilitando así las tareas posteriores.

Una técnica común de preprocesamiento es el uso de **filtros**, que modifican los valores de los píxeles en función de sus vecinos para suavizar, eliminar ruido o resaltar bordes.

---

### ¿Qué es un filtro?

Un filtro es una operación matemática que aplica un **núcleo (kernel)** o máscara a una imagen, modificando cada píxel según una función que considera los píxeles vecinos.

- **Filtros lineales**: realizan una operación ponderada y sumatoria (ejemplo: filtro gaussiano).
- **Filtros no lineales**: usan estadísticas como la mediana para determinar el nuevo valor (ejemplo: filtro de mediana).

---

### Filtro Gaussiano

El filtro gaussiano es un filtro lineal que aplica la función de distribución gaussiana para suavizar la imagen.

\[
G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
\]

Donde:
- \( x, y \) son las coordenadas dentro del kernel.
- \( \sigma \) es la desviación estándar que controla la intensidad del suavizado.

**Beneficios:**
- Reduce el ruido de alta frecuencia.
- Suaviza la imagen preservando las estructuras generales.

---

### Filtro de Mediana

El filtro de mediana es un filtro no lineal que reemplaza cada píxel por la mediana de los valores de sus píxeles vecinos.

**Beneficios:**
- Excelente para eliminar ruido tipo “sal y pimienta”.
- Preserva bordes mejor que los filtros lineales.

---

### Filtro Combinado

Aplicar primero un filtro gaussiano y luego un filtro de mediana combina las ventajas de ambos métodos, logrando una mejor reducción de ruido y preservación de detalles.

---

### Código explicado paso a paso

```python
import cv2

# Crear ventanas para mostrar las imágenes
cv2.namedWindow("Original")
cv2.namedWindow("Filtro Gaussiano")
cv2.namedWindow("Filtro de Mediana")
cv2.namedWindow("Filtro Combinado")

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar para mejorar rendimiento
    frame = cv2.resize(frame, (320, 240))

    # Aplicar filtro gaussiano (kernel 3x3, sigma 1.4)
    gauss = cv2.GaussianBlur(frame, (3, 3), 1.4)

    # Aplicar filtro de mediana (kernel 3x3)
    mediana = cv2.medianBlur(frame, 3)

    # Aplicar filtro combinado (gaussiano + mediana 5x5)
    combinado = cv2.medianBlur(gauss, 5)

    # Mostrar resultados
    cv2.imshow("Original", frame)
    cv2.imshow("Filtro Gaussiano", gauss)
    cv2.imshow("Filtro de Mediana", mediana)
    cv2.imshow("Filtro Combinado", combinado)

    # Salir al presionar ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
