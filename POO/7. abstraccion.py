from abc import ABC, abstractmethod

# clase abstracta
class EstructuraAbstracta(ABC):
  @abstractmethod
  # no hay implementaciones
  def obtener():
    pass

  @abstractmethod
  # no debe tener implementaciones
  def agregar():
    pass  

class Hash(EstructuraAbstracta):
  # clase genérica
  datos = {}

  def obtener(self,llave):
    datos[llave]
  
  def agregar(self,llave,valor):
    datos[llave] = valor

class Queue(EstructuraAbstracta):
  # clase genérica
  datos = []

  def obtener(self):
    datos[0]
  
  def agregar(self,llave,valor):
    datos[len(datos)-1] = valor

# creas una clase concreta, que va a definir o rellenar algo a partir de clases genéricas con diferentes configuraciones. Con ello modificas la clase concreta sin modificar su estructura.



class FilaBanco:
  # clase concreta
  def __init__(self,almacen_usuarios):
    if not isinstance (almacen_usuarios, EstructuraAbstracta):
      raise ValueError('No lo soporta el repositorio')
    self.usuarios = almacen_usuarios

  def siguiente_usuario(self,numero):
    # implementación
    return self.usuarios.obtener(numero)

  def formar_usuario(self,numero,usuario):
    self.usuarios.agregar(numero,usuario)

FilaBanco(Hash())
