# simpleImage

Paquete Python para cargar y manipular imágenes píxel a píxel, inspirado en los "Image Puzzles" de Nick Parlante (Stanford Nifty Assignments, 2011).

---

## Descripción

`simpleImage` proporciona clases (`SimpleImage` y `Pixel`) para:

- Cargar imágenes que residen en el subdirectorio `images/`.
- Visualizarlas en ventana mediante Tkinter.
- Acceder y modificar cada canal de color (RGB/RGBA) por coordenadas.
- Recorrer todos los píxeles de forma natural con `for pixel in img:`.

---

## Estructura del proyecto

```
simpleImage/            # Paquete principal
├── __init__.py         # Exporta SimpleImage y Pixel
├── SimpleImage.py      # Implementación de clases
└── images/             # Carpeta con imágenes de ejemplo
    ├── flowers.jpg
    └── iron-puzzle.png

example_usage.py        # Ejemplo de uso del paquete
README.md               # Este archivo
requirements.txt        # Dependencias del proyecto
```

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <repo_url>
   cd simpleImage
   ```
2. Instala dependencias localmente:
   ```bash
   pip3 install --user -r requirements.txt
   ```

   Si lo anterior no funciona, entonces intenta esto:

   ```bash
   pip3 install --user --break-system-packages -r requirements.txt
   ```

   Es posible que nada de lo anterior funcione en ubuntu, por lo que se tendría que ejecutar esta línea:

   ```bash
   sudo apt install python3-pil python3-pil.imagetk
   ```

---

## Uso básico

```python
from simpleImage import SimpleImage

# Carga "flowers.jpg" desde images/
img = SimpleImage("flowers.jpg")

img.print()

```

---

## Documentación de la API

### Paquete `simpleImage`

**Importación recomendada:**
```python
from simpleImage import SimpleImage, Pixel
```

El paquete incluye:
- `simpleImage/SimpleImage.py`: implementación de las clases `SimpleImage` y `Pixel`.

---

### Clase `SimpleImage`

#### Constructor
```python
SimpleImage(filename: str)
```
Carga la imagen (en `images/`) con el nombre dado y prepara el acceso a sus píxeles.

#### Métodos públicos

```python
save(outputPath: str)
```
Guarda la imagen actual en la ruta indicada.

```python
print()
```
Muestra la imagen en una ventana Tkinter y bloquea hasta que el usuario la cierre.

```python
getWidth() -> int
```
Devuelve el ancho de la imagen en píxeles.

```python
getHeight() -> int
```
Devuelve el alto de la imagen en píxeles.

```python
getPixel(x: int, y: int) -> Pixel
```
Retorna un objeto `Pixel` correspondiente a la coordenada `(x, y)`.

```python
getRed(x: int, y: int) -> int
getGreen(x: int, y: int) -> int
getBlue(x: int, y: int) -> int
```
Devuelven el valor de cada componente de color (R, G, B) en el píxel `(x, y)`.

```python
setRed(x: int, y: int, value: int)
setGreen(x: int, y: int, value: int)
setBlue(x: int, y: int, value: int)
```
Asignan `value` al canal correspondiente del píxel `(x, y)`. Para imágenes con canal alfa, preservan los valores adicionales.

---

### Clase `Pixel`

Los píxeles sólo serán directamente accedidos en dos casos:
1. Cuando se itere sobre todos los pixeles de una imagen sin importar su posición en la foto.

```python
for pixel in image:
  pixel....
```
2. Usando el método getPixel con las coordenadas específicas del pixel en la imagen.

```python
pixel = image.getPixel(10, 13)
```
#### Métodos públicos

```python
getRed() -> int
getGreen() -> int
getBlue() -> int
```
Devuelven el valor de cada canal del píxel.

```python
setRed(value: int)
setGreen(value: int)
setBlue(value: int)
```
Asignan `value` al canal correspondiente, preservando otros componentes (como alfa).

---

## Licencia

MIT License © 2025
