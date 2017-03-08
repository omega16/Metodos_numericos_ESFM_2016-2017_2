#!/usr/bin/env python3


import modulo as nt

"""

Programa echo por : Omega16
Boleta : censurado 
Programa creado para la clase métodos numéricos impartida en la ESFM-IPN periodo 2016-2017 2 , Domingo 19 de febrero de 2017
Proposito:

    Este programa calcula las raices de la funcion (sin(x)* (x**3) )- log(np.abs(cos(x))) - x**(7/8) - 1/(x**2 -3*x -3) -24.8
    
El programa esta echo de forma que editando las funciones funcion_clase y deriva_funcion_clase se puede usar el metodo de newton en otras funciones.
    
Forma de ejecucion recomendada :

    python3 -W ignore driver.py iter eps a b N bo ruta
    
     -iter(int)        Numero_maximo_de_iteraciones
     -eps(float64)     epsilon del algorimto de newton
     -a(int)           extremo_izquierdo_de_intervalo 
     -b(int)           extremo_derecho_de_intervalo 
     -N(int)           Se particionara el intervalo (a,b) en N partes
     -bo(0/1)          Imprime lineas de estetica en el archivo de salida si es 1, si es 0 las omite               
     -ruta(str)        /Ruta/Absoluta/a/archivo/de/salida/salida_newton.txt
    
    
    Nota: se necesita -W ignore para sumprimir alertas (que estan controladas dentro del programa) 
    
Ejemplo de ejecucion (parametros recomendados) : 

    python -W ignore driver.py 50 1e-12 4 800 400 0 '/Ruta/Absoluta/a/archivo/de/salida/salida_newton.txt'
    
   Calcula las raices en el intervalo (4,800) usando el algoritmo de newton sobre 400 intervalos (particion de 400 partes de (4,800)) con un maximo de iteraciones de 50 y un epsilon de 1X10^(-12) , sin imprimir lineas esteticas en la salida que se encuentra en /Ruta/Absoluta/a/archivo/de/salida/salida_newton.txt
    
"""



nt.testmethod(nt.funcion_clase,nt.deriva_funcion_clase)
