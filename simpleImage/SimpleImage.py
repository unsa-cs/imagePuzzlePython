import os
from PIL import Image
from typing import Tuple
import tkinter as tk
from PIL import ImageTk

class Pixel:
  def __init__(self, x: int, y: int, image: 'SimpleImage'):
    """Vincula el Pixel a su SimpleImage y coordenadas."""
    self.x = x
    self.y = y
    self._image = image

  def getRed(self) -> int:
    return self._image._pixels[self.x, self.y][0]

  def getGreen(self) -> int:
    return self._image._pixels[self.x, self.y][1]

  def getBlue(self) -> int:
    return self._image._pixels[self.x, self.y][2]

  def setRed(self, x: int, y: int, value: int) -> None:
    """Asigna el canal rojo, preservando canales restantes incluida alpha."""
    _, g, b, *rest = self._image._pixels[x, y]
    self._image._pixels[x, y] = (value, g, b, *rest)

  def setGreen(self, x: int, y: int, value: int) -> None:
    """Asigna el canal verde, preservando canales restantes incluida alpha."""
    r, _, b, *rest = self._image._pixels[x, y]
    self._image._pixels[x, y] = (r, value, b, *rest)

  def setBlue(self, x: int, y: int, value: int) -> None:
    """Asigna el canal azul, preservando canales restantes incluida alpha."""
    r, g, _, *rest = self._image._pixels[x, y]
    self._image._pixels[x, y] = (r, g, value, *rest)

  def getColor(self) -> Tuple[int, ...]:
    """Devuelve una tupla con los canales del píxel (RGB o RGBA)."""
    return self._image._pixels[self.x, self.y]

  def __repr__(self) -> str:
    cols = self.getColor()
    return f"Pixel(x={self.x}, y={self.y}, color={cols})"

class SimpleImage:
  def __init__(self, filename: str):
    """Carga la imagen ubicada en el directorio 'images' con el nombre dado."""
    images_dir = os.path.join(os.getcwd(), 'images')
    full_path = os.path.join(images_dir, filename)
    self._image = Image.open(full_path)
    self._pixels = self._image.load()

  def save(self, outputPath: str):
    """Guarda la imagen en la ruta indicada."""
    self._image.save(outputPath)

  def print(self):
    """Muestra la imagen en una ventana Tkinter y bloquea hasta cerrar."""
    root = tk.Tk()
    root.title("SimpleImage")
    tk_img = ImageTk.PhotoImage(self._image)
    label = tk.Label(root, image=tk_img)
    label.pack()
    label.image = tk_img
    root.mainloop()

  def __str__(self) -> str:
    return f"SimpleImage {self.getWidth()}×{self.getHeight()}"

  def getWidth(self) -> int:
    """Ancho de la imagen en píxeles."""
    return self._image.width

  def getHeight(self) -> int:
    """Alto de la imagen en píxeles."""
    return self._image.height

  def getPixel(self, x: int, y: int) -> Pixel:
    """Devuelve el Pixel en la posición (x, y)."""
    return Pixel(x, y, self)

  def getRed(self, x: int, y: int) -> int:
    """Devuelve el canal rojo en (x, y)."""
    return self._pixels[x, y][0]

  def getGreen(self, x: int, y: int) -> int:
    """Devuelve el canal verde en (x, y)."""
    return self._pixels[x, y][1]

  def getBlue(self, x: int, y: int) -> int:
    """Devuelve el canal azul en (x, y)."""
    return self._pixels[x, y][2]

  def setRed(self, x: int, y: int, value: int) -> None:
    """Atajo para asignar solo el canal rojo."""
    Pixel(x, y, self).setRed(x, y, value)

  def setGreen(self, x: int, y: int, value: int) -> None:
    """Atajo para asignar solo el canal verde."""
    Pixel(x, y, self).setGreen(x, y, value)

  def setBlue(self, x: int, y: int, value: int) -> None:
    """Atajo para asignar solo el canal azul."""
    Pixel(x, y, self).setBlue(x, y, value)

  def __iter__(self):
    """Itera sobre todos los píxeles de la imagen."""
    for y in range(self.getHeight()):
      for x in range(self.getWidth()):
        yield self.getPixel(x, y)
