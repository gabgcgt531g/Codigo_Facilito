class Usuario:
  def __init__(self, nombre):
    # metodo constructor
    self.nombre = nombre

    
  def saludar(self, saludo):
    # self nos permite identifcar al objeto con el que estamos trabajando, pero dentro de la clase.
    print(saludo + self.nombre)

usuario = Usuario ("Gabi")
usuario.saludar ("Que tal ")