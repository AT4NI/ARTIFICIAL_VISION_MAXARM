\# Clasificación de Objetos por Color y Forma usando OpenCV



\## Descripción



Este proyecto implementa un sistema de visión artificial capaz de detectar, segmentar y clasificar objetos en tiempo real según su color y forma geométrica. Utiliza una cámara para capturar imágenes, procesa la información en el espacio de color HSV, y aplica técnicas avanzadas de filtrado y análisis de contornos para reconocer figuras como triángulos, cuadrados, trapecios, rombos y hexágonos, diferenciando además entre varios colores calibrados.



---



\## Conceptos Fundamentales



\### Espacio de color HSV



El modelo HSV representa los colores mediante tres componentes:



\- \*\*Hue (tono):\*\* indica el color base, medido en grados (0-179 en OpenCV).

\- \*\*Saturation (saturación):\*\* indica la intensidad del color.

\- \*\*Value (valor):\*\* representa el brillo o luminosidad.



Esta representación facilita la segmentación de colores bajo diferentes condiciones de iluminación.



\### Filtros Morfológicos



Operan sobre imágenes binarias para limpiar ruido y mejorar la calidad de las máscaras:



\- \*\*Apertura:\*\* elimina pequeños ruidos.

\- \*\*Cierre:\*\* rellena pequeños huecos en los objetos detectados.



\### Filtros de Suavizado



\- \*\*Filtro Gaussiano:\*\* reduce el ruido suavizando la imagen.

\- \*\*Filtro de Mediana:\*\* elimina ruido impulsivo preservando bordes.



\### Cálculo de Ángulos Internos



Los ángulos internos de un polígono se calculan para diferenciar entre distintas formas geométricas con igual número de lados. Se obtienen midiendo el ángulo formado por dos vectores que parten de cada vértice.



\### Pendientes y Paralelismo



El paralelismo entre lados se determina calculando las pendientes y comparándolas con un umbral para detectar figuras como rectángulos y trapecios.



---



\## Funcionamiento del Código



\### 1. Importación y calibración de rangos HSV



Se definen rangos específicos en HSV para colores como azul, verde, rojo, amarillo, naranja y tonos carne, para segmentar correctamente cada color en la imagen capturada.



\### 2. Cálculo de ángulos y pendientes



Funciones para calcular los ángulos internos de polígonos y pendientes de sus lados, que son clave para clasificar la forma geométrica detectada.



\### 3. Clasificación de formas



La función `detectar\_forma` analiza:



\- Número de vértices.

\- Lados y ángulos internos.

\- Paralelismo entre lados.

\- Relación de aspecto.



Para distinguir entre triángulos, cuadrados, trapecios, rombos y hexágonos, considerando también deformaciones y tolerancias.



\### 4. Captura y procesamiento de video



\- Se abre la cámara y se captura imagen en tiempo real.

\- La imagen se convierte a espacio HSV para facilitar la segmentación por color.

\- Para cada color calibrado, se crea una máscara binaria.



\### 5. Preprocesamiento de máscaras



\- Se aplican filtros morfológicos (apertura y cierre) para eliminar ruido y rellenar huecos.

\- Se aplican filtros Gaussiano y de Mediana para suavizar y mejorar la máscara.



\### 6. Detección de contornos y clasificación



\- Se extraen contornos de la máscara.

\- Se filtran por área para eliminar pequeños objetos.

\- Se aproxima el contorno a un polígono para determinar la forma.

\- Se dibujan contornos, etiquetas de color y forma, y rectángulos delimitadores en la imagen resultado.



\### 7. Visualización



\- Se muestran tres ventanas: la imagen original, la máscara preprocesada y el resultado con objetos detectados y clasificados.

\- El proceso se ejecuta hasta que se presiona la tecla `s` para salir.



