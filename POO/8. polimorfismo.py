def retornaElMayor(a,b):
  # instance()
  if isinstance(a,int) and isinstance(b,int):
    # si son enteros
    if a > b:
      return a
    return b
  
  if isinstance(a,str) and isinstance(b,str):
    # si son cadenas
    palabras = [a,b]
    palabras.sort()
    return palabras [0]
    # ordena alfabéticamente, metiendo los valores en un array y llamando a metodo sort con valor cero para coger el primero o mayor.

  if isinstance(a,list) and isinstance(b,list):
    # si es una lista (array)
    if len(a) > len(b):
      # coge el array que mayor longitud tiene
      return a
    return b

print(retornaElMayor(10,14))
print(retornaElMayor( "Gabri","Alex"))
print(retornaElMayor( [1,2],[1,2,3]))