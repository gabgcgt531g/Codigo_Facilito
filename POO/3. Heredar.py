class Usuario:
  def __init__(self, nombre):
    # metodo constructor
    self.nombre = nombre
    
  def saludar(self, saludo):
    # self nos permite identifcar al objeto con el que estamos trabajando, pero dentro de la clase.
    
    print(saludo + self.nombre)

class Empleado (Usuario):
  # clase hijo, hereda propiedades de Usuario
  salario = 0
  
  def modificar_salario(self, salario):
    self.salario = salario
  
  def ver_salario(self):
    print(self.salario)

# usuario = Usuario("Leti")
# usuario.ver_salario("Salario Leti: ")
# # sale error, esta propiedad no esta en clase Usuario, si no en su hijo.

empleado = Empleado("Gabi")
empleado.saludar("Hola, me llamo ")
empleado.modificar_salario(19000/14)
empleado.ver_salario()