def saludo(nombre):
  return"Hola {}, bienvenido.".format(nombre)
  # devuelve valores. Deja un hueco entre corchetes, que será lo que definimos con format
print("Introduce tu nombre: ")
nombre = input()
# declaramos el valor introducido por el usuario
print (saludo (nombre))
# no hay que especificar el tipo de dato, porque son todo strings