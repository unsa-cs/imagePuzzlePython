import tkinter as tk
from PIL import Image, ImageTk

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

  def setRed(self, value: int) -> None:
    _, g, b = self._image._pixels[self.x, self.y]
    self._image._pixels[self.x, self.y] = (value, g, b)

  def setGreen(self, value: int) -> None:
    r, _, b = self._image._pixels[self.x, self.y]
    self._image._pixels[self.x, self.y] = (r, value, b)

  def setBlue(self, value: int) -> None:
    r, g, _ = self._image._pixels[self.x, self.y]
    self._image._pixels[self.x, self.y] = (r, g, value)

  def getColor(self) -> tuple[int, int, int]:
    return self._image._pixels[self.x, self.y]

  def __repr__(self) -> str:
    r, g, b = self.getColor()
    return f"Pixel(x={self.x}, y={self.y}, r={r}, g={g}, b={b})"

class SimpleImage:
  def __init__(self, filepath: str):
    """Carga imagen desde disco y prepara píxeles."""
    self._image = Image.open(filepath)
    self._pixels = self._image.load()

  def save(self, outputPath: str):
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
    return self._image.width

  def getHeight(self) -> int:
    return self._image.height

  def getPixel(self, x: int, y: int):
    return Pixel(x, y, self)

  def getRed(self, x: int, y: int) -> int:
    return self._pixels[x, y][0]

  def getGreen(self, x: int, y: int) -> int:
    return self._pixels[x, y][1]

  def getBlue(self, x: int, y: int) -> int:
    return self._pixels[x, y][2]

  def setRed(self, x: int, y: int, value: int):
    _, g, b = self._pixels[x, y]
    self._pixels[x, y] = (value, g, b)

  def setGreen(self, x: int, y: int, value: int):
    r, _, b = self._pixels[x, y]
    self._pixels[x, y] = (r, value, b)

  def setBlue(self, x: int, y: int, value: int):
    r, g, _ = self._pixels[x, y]
    self._pixels[x, y] = (r, g, value)

  def __iter__(self):
    for y in range(self.getHeight()):
      for x in range(self.getWidth()):
        yield self.getPixel(x, y)
