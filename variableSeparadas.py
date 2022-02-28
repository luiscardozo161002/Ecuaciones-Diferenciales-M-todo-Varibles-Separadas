#Importamos e inicializamos el módulo a usar para relizar la parte de las derivadas y las integrales
import sympy as sp
from sympy import integrate, init_printing
from sympy.abc import x
init_printing(use_latex="mathjax")
#Importamos el modulo para graficar la parte de la ecuación diferencial
import matplotlib.pyplot as plt
import numpy as np


#Imprimimos el mensaje de la derivada como primer paso para la resolucion del problema
print("Derivamos la ecuacion diferencial")
#Definimos la variable simbolica en este caso t
x = sp.Symbol('t') 
#Ingresamos la ecuación diferencial
y = input(str("Ingrese la ecuación diferencial: ")) # t**3+2*t**2+t-1
#Imprimos el resultado de la derivada
print("El resultado de la ecuacion diferencial: ")
print(sp.diff(y,x)) 
#Para la integral solo tomamos la ecuacion diferencial y la integramos
integral=y
#Imprimimos el mensaje del resultado de la temperatura/tiempo (integral definida)
print("El resultado de la temperatura/tiempo: ")
print(sp.integrate(y,(x,0,20)))

#Valores del resultado de la tabulación
lista1 = [0,2.6,5.2,7.8,10.4,13.6,15.6,23.4,28.6,31.4,36.5,39.7,40.9,46.8,53.8,56.7,63.9,66.5,68.9,69.6,70]
#Grafica la lista con los valores
plt.plot(lista1) 
plt.title("Grafico de la Temperatura/tiempo")   # Establece el título del gráfico
plt.xlabel("Tiempo- Seg")   # Establece el título del eje x
plt.ylabel("Temperatura- °C ")   # Establece el título del eje y
plt.show()#Ejecuta y grafica la parte de la grafica
