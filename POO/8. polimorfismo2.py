# manera mas extensa pero versátil
class Numero:
  value = 0
  def __init__(self,value):
    self.value = value
  
  def compare(self,numero):
    if numero.value > self.value:
      return numero.value
    return self.value

class Cadena:
  value = ""
  def __init__(self,value):
    self.value = value

  def compare(self,cadena):
    palabras = [self.value,cadena.value]
    palabras.sort()
    return palabras [0]

class Lista:
  value = []
  def __init__(self,value):
    self.value = value

  def compare(self,lista):
    if len(self.value) > len(lista.value):
      # coge el array que mayor longitud tiene
      return self.value
    return lista.value
     

def retornaElMayor(a,b):
  return a.compare(b)

numero_uno = Numero(10)
numero_dos = Numero(14)

cadena_uno = Cadena("Gabi")
cadena_dos = Cadena("Alex")

lista_uno = Lista([1,2,3])
lista_dos = Lista([1,2,3,4])

print(retornaElMayor(numero_uno,numero_dos))
print(retornaElMayor(cadena_uno, cadena_dos))
print(retornaElMayor(lista_uno,lista_dos))