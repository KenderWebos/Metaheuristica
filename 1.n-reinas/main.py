import time
import random

cantidadReinas = 8
largoTablero = 8
anchoTablero = 8

poblacionInicial = []

def GenerarPoblacionInicial(poblacion):
    poblacion += [1, 2, 3, 4, 5, 6, 7, 8]
    poblacion += [1, 2, 3, 4, 5, 6, 7, 8]
    poblacion += [1, 2, 3, 4, 5, 6, 7, 8]

GenerarPoblacionInicial(poblacionInicial)

print(poblacionInicial)

def init():
    return "algoritmo completado"