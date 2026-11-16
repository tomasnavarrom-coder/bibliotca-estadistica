%%writefile calest.py

def media(datos): 
  suma = 0
  for x in datos:
    suma = suma + x
  return suma/len(datos)

def de(datos):
  m = media(Datos)
  suma_cuadrados = 0
  for x in datos:
    suma_cuadrados = suma_cuadrados + (x - m)**2
  return (suma_cuadrados/len(datos)**0.5)
