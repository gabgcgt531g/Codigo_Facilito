class Usuario:
  def __init__(self, nombre): 
    #metodo constructor   
    self._nombre = nombre
    
  def saludar(self, saludo): 
    print(saludo + self.nombre)

  __edad = 0

  @property
  def edad (self): #getter
    return self.__edad
    # creamos una propiedad edad, igual que __edad pero no es privada. para poder trabajar con ella y editar y darle condiciones pero las unimos.

  @edad.setter
  def edad (self,valor):
    if (valor < 0):
      raise ValueError ('Edad no puede ser menor que 0')
    self.__edad = valor

class Empleado (Usuario):
  __salario = 0  
  
  def modificar_salario(self, salario): #setter
    self.__salario = salario
  
  def ver_salario(self): #getter
    print(self.__salario)

  def saludar (self):
    super().saludar("Hola ")
    print("Mi salario es: "+str(self._nombre)+" y gano: "+str(self.__salario))

empleado = Empleado("Gabi")
empleado.edad = -1
print (empleado.edad)