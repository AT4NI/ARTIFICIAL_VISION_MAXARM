## Concepto
### HSV
Las siglas significan: Hue (tono), Saturation (saturación), Value (valor o brillo). Es un **modelo de color para procesamiento de imágenes**, porque separa la información del color (tono) de la intensidad (saturación y brillo).

- Hue (tono): representa el color, se mide en grados (0 a 179 en OpenCV, donde 0° es rojo, ~60° es amarillo, ~120° es verde, ~180° es azul, etc.).
- Saturation (saturación): qué tan puro es el color (0 a 255). Un valor bajo indica un color grisáceo, uno alto es color intenso.
- Value (valor o brillo): qué tan claro u oscuro es el color (0 a 255). 0 es negro, 255 es brillo máximo.

Usamos HSV porque es más robusto para detectar colores que el modelo RGB/BGR clásico, que es sensible a cambios de luz.

#### Developing...
