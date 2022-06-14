class page:
  def print_footer(self):
    print("Hola")

class legalpage (page):
  def print_footer(self):
    print("Mundo")
    super().print_footer()
