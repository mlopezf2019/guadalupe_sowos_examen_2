def saludo(f):
  def wrapper(nombre):
    print('Hola: ')
    result = f(nombre)
    return result
  
  return wrapper

@saludo
def saludar(nombre):
  return nombre

print(saludar('Lupita'))