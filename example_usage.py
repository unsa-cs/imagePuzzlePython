from simpleImage import SimpleImage

def main():
  # Carga la imagen "iron-puzzle.png"
  img = SimpleImage("iron-puzzle.png")

  # Muestra la imagen en ventana
  img.print()

  # Aplica una transformación: invierte el canal rojo de cada pixel
  for pixel in img:
    r = pixel.getRed()
    pixel.setRed(255 - r)

  # Guarda el resultado en un nuevo archivo
  img.save("iron-solution.png")

  # Imprime información de la imagen
  print(img)

if __name__ == "__main__":
  main()
