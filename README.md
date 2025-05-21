# simpleImage

Paquete Python para cargar y manipular imágenes píxel a píxel, inspirado en los "Image Puzzles" de Nick Parlante (Stanford Nifty Assignments, 2011).

---

## Descripción

`simpleImage` proporciona clases sencillas (`SimpleImage` y `Pixel`) para:

- Cargar imágenes desde archivos.
- Visualizarlas en ventana mediante Tkinter.
- Acceder y modificar cada canal de color (RGB) por coordenadas.
- Recorrer todos los píxeles de forma natural con `for pixel in img:`.

Adaptación en Python del material original de Nick Parlante:
http://nifty.stanford.edu/2011/parlante-image-puzzle/

---

## Estructura del proyecto

```
simpleImage/         # Paquete principal
├── __init__.py      # Exporta SimpleImage y Pixel
└── SimpleImage.py   # Implementación de clases

images/              # Ejemplos de imagens
example.py           # Ejemplo de uso del paquete
README.md            # Este archivo
requirements.txt     # Dependencias del proyecto
```

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <repo_url>
   cd simpleImage
   ```
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

**requirements.txt** debe incluir:
```
pillow
```

---

## Uso básico

```python
from simpleImage import SimpleImage

# Carga la imagen
img = SimpleImage("iron-puzzle.png")

# Muestra en ventana
img.print()

# Procesa píxel a píxel
for pixel in img:
  r = pixel.getRed()
  pixel.setRed(0)

# Guarda resultado
img.save("iron-solution.png")
```

---

## Documentación de la API

Consulta `API_Documentation.md` para referencia completa de clases y métodos públicos.

---

## Licencia

MIT License © 2025
