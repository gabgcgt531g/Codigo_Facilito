class Usuario:
# define la clase
  nombre = "facebook"     
  def saludar(self, saludo):
    # self nos permite identifcar al objeto con el que estamos trabajando, pero dentro de la clase.
    print(saludo + self.nombre)

facebook = Usuario()
# nombra el objeto y lo relaciona con la clase
facebook.nombre = "Gabi"
# le da una propiedad al objeto
facebook.saludar("Hola, que tal ")