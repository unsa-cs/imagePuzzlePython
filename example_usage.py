from simpleImage import SimpleImage

def main():
  # Carga la imagen "iron-puzzle.png"
  img = SimpleImage("flowers.png")

  # Muestra la imagen en ventana
  img.print()

  # Imprime información de la imagen
  print(img)

if __name__ == "__main__":
  main()
