class Usuario:
  def __init__(self, nombre):
    # metodo constructor
    self.nombre = nombre
    
  def saludar(self, saludo):
    # self nos permite identifcar al objeto con el que estamos trabajando, pero dentro de la clase.    
    print(saludo + self.nombre)

class Empleado (Usuario):
  # clase hijo, hereda propiedades de Usuario
  salario = 1000
  
  def modificar_salario(self, salario):
    self.salario = salario
  
  def ver_salario(self):
    print(self.salario)

  def saludar (self):
    super().saludar("Hola ")
    # trae la funcionalidad del método de la clase padre
    print("Mi salario es: "+str(self.nombre)+" y gano: "+str(self.salario))
    # y ejecuta tb la funcionalidad de la clase hija

empleado = Empleado("Gabi")
empleado.saludar()

class Pagina:
  def imprimir_pie_pag (self):
    print (self.pie_pagina)

class PaginaLegal (Pagina):
  def imprimir_pie_pag (self):
    # sobreescribo el método de la clase padre
    print ("Derechos reservados")
    super().imprimir_pie_pag()
    # accedo al método de la calse padre aun sobreescribiendo en la clase hijo

html = PaginaLegal()
html.pie_pagina = "<p> Hola </p>"
html.imprimir_pie_pag()