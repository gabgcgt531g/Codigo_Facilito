class Usuario:
  def __init__(self, nombre):
    # metodo constructor
    self._nombre = nombre
    # si la propiedad empieza por un guión bajo, nos dice que es PROTEGIDA, aunque no da error al ejecutarlo
    
  def saludar(self, saludo):
    # self nos permite identifcar al objeto con el que estamos trabajando, pero dentro de la clase.    
    print(saludo + self.nombre)

class Empleado (Usuario):
  # clase hijo, hereda propiedades de Usuario
  __salario = 0
  # si la propiedad empieza por doble guión bajo, nos dice que es PRIVADA
  
  def modificar_salario(self, salario):
    # setter: altera o asigna un nuevo valor a la propiedad __salario
    self.__salario = salario
  
  def ver_salario(self):
    # getter: obtiene el valor actual de la propiedad __salario
    print(self.__salario)

  def saludar (self):
    super().saludar("Hola ")
    # trae la funcionalidad del método de la clase padre
    print("Mi salario es: "+str(self._nombre)+" y gano: "+str(self.__salario))
    # y ejecuta tb la funcionalidad de la clase hija

empleado = Empleado("Gabi")
empleado.modificar_salario(1650)
empleado.ver_salario()
# se puede utilizar esta variable desde otra instancia, atribuyendo otro valor
print (empleado.__salario)
# si ejecutamos la propiedad salario, al estar privada, nos dice que no existe
