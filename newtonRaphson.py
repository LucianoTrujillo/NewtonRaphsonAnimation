import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
from prettytable import PrettyTable

#obtiene el error de la máquina dependiendo de la representacion de punto flotante
def obtener_error_maquina(usar32Bit):
  if usar32Bit:
    return 10**(-np.finfo(np.float32).precision)
  return 10**(-np.finfo(np.float).precision)

#casteos a float 32
def obtenerPrecision(numero, usar32Bit):
    if usar32Bit:
      return np.float32(numero)
    return numero

#obtención de float más pequeño para cortar algoritmos
def obtenerFloatMinimo(usar32Bit):
  if usar32Bit:
    return np.finfo(np.float32).tiny
  return np.finfo(np.float).tiny


def tablaNewtonRaphson(funcion, funcionDerivada, candidataRaiz, tolerancia, cantidadIteracionesPermitidas, usar32Bit):
  iteracionActual = 1
  errorEntreIteraciones = 0
  filas = cantidadIteracionesPermitidas + 1
  columnas = 3
  tabla = np.zeros((filas, columnas), dtype=(np.float32 if usar32Bit else np.float64))
  tabla[0] = (0, candidataRaiz, None)
  floatMinimo = obtenerFloatMinimo(usar32Bit)

  def terminarBusquedaYdevolverDatosNewtonRaphson():
    return tabla[:iteracionActual + 1]

  while iteracionActual <= cantidadIteracionesPermitidas:

    if np.abs(funcionDerivada(candidataRaiz)) <= floatMinimo:
      print("\terror NewtonRaphson: La derivada se anula en el punto", candidataRaiz)
      candidataRaiz = None
      return terminarBusquedaYdevolverDatosNewtonRaphson()
  
    nuevaCandidataRaiz = obtenerPrecision(candidataRaiz - funcion(candidataRaiz)/funcionDerivada(candidataRaiz), usar32Bit)
    errorEntreIteraciones = obtenerPrecision(np.abs((candidataRaiz - nuevaCandidataRaiz) / nuevaCandidataRaiz), usar32Bit)

    if ((math.isinf(funcion(candidataRaiz))) or (math.isinf(funcionDerivada(candidataRaiz)))):
      printf('\terror NewtonRaphson: No pudo ejecutarse el calculo con los numeros pedidos, debido a que no existe dicha funcion en el punto, ultima semilla: ', semilla)
      candidataRaiz = None      
      return terminarBusquedaYdevolverDatosNewtonRaphson()

    tabla[iteracionActual] = (
        iteracionActual,
        nuevaCandidataRaiz,
        obtener_error_maquina(usar32Bit) if errorEntreIteraciones == 0 else errorEntreIteraciones)

    if funcion(nuevaCandidataRaiz) == 0.0: 
      errorEntreIteraciones = floatMinimo
      return terminarBusquedaYdevolverDatosNewtonRaphson()

    if errorEntreIteraciones <= tolerancia:
      return terminarBusquedaYdevolverDatosNewtonRaphson()

    iteracionActual += 1
    candidataRaiz = nuevaCandidataRaiz
    
  
  print("\terror NewtonRaphson: No se encontró la raiz luego de", cantidadIteracionesPermitidas, "iteraciones")
  return terminarBusquedaYdevolverDatosNewtonRaphson()

def animacionNewtonRaphson(funcion, funcionDerivada, aproximacionInicial, xMenor=-10, xMayor=10, yMenor=-10, yMayor=10, puntos=1000, tolerancia=0.001, maximasIteracionesPermitidas=100, zoom=1, tamanioEnPulgadas=10, bitsDeMaquina=64, label="Newton Raphson"):
  usa32Bit = True if bitsDeMaquina == 32 else False
  tabla = tablaNewtonRaphson(funcion, funcionDerivada, aproximacionInicial, tolerancia, maximasIteracionesPermitidas, usa32Bit)

  valoresQueTomaX = np.linspace(xMenor, xMayor, puntos)
  fig, ax = plt.subplots(figsize=(tamanioEnPulgadas, tamanioEnPulgadas))
  ax = plt.axes(xlim=(xMenor/zoom, xMayor/zoom), ylim=(yMenor/zoom, yMayor/zoom))
  rectaTangente, = ax.plot([], [], label='recta tangente en raiz', lw=2, animated=True)
  lineaFuncion, = ax.plot(valoresQueTomaX, funcion(valoresQueTomaX), color='black', lw=1.5)
  ejex, = ax.plot([], [], color='gray', lw=1)
  rectaVerticalRaiz = ax.axvline(tabla[0][1], ls='-', color='r', lw=1, zorder=10)

  #Printeo de raices
  rangos = np.zeros(len(tabla))
  for i, fila in enumerate(tabla):
    rangos[i] = fila[1]
    plt.plot(fila[1],0,'ro') 

  #Funcion creadora de rectas tangentes
  def crearRectaTangente(funcion, funcionDerivada, raiz):
    def recta(x):
      return funcionDerivada(raiz)*(x-raiz) + funcion(raiz)
    return recta

  #Inicializacion
  def init():
      rectaTangente.set_data([], [])
      ejex.set_data(valoresQueTomaX, np.zeros(puntos))
      lineaFuncion.set_data(valoresQueTomaX, funcion(valoresQueTomaX))
      return rectaTangente, ejex, lineaFuncion, rectaVerticalRaiz,

  #Animacion <- se llama en cada frame
  def animate(i):
    fila = tabla[i]
    rectaTangenteEnPunto = crearRectaTangente(funcion, funcionDerivada, fila[1])
    label = 'tangente en ' + str(fila[1])
    rectaTangente.set_data(valoresQueTomaX, rectaTangenteEnPunto(valoresQueTomaX))
    a = rangos[i]
    rectaVerticalRaiz.set_data( [a, a], [-1, 1])
    return rectaTangente, ejex, lineaFuncion, rectaVerticalRaiz,

  #Metadata
  plt.xlabel('x')
  plt.ylabel('funcion(x)')
  plt.title(label)
  plt.axis([xMenor/zoom, xMayor/zoom, yMenor/zoom, yMayor/zoom])
  plt.legend(loc='best')
  plt.grid(True)

  animacion = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(tabla), interval=1000, blit=True)
  rc('animation', html='jshtml')
  return animacion
