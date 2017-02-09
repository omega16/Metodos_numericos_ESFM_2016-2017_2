#!/usr/bin/env python3



import sys
import sympy

"""

Programa echo por : Luis Alberto Díaz Díaz
Boleta : 2014330326
Programa creado para la clase métodos numéricos impartida en la ESFM-IPN periodo 2016-2017 2 , miercoles 8 de febrero de 2017
Proposito:

    Este programa calcula el polinomio P_n de Taylor de una funcion al rededor de un punto x0 y aproxima el valor de algun otro punto x
    
Forma de ejecucion :

    ./driver.py "f(x)= " x0 x n
    
    Nota: El programa solo admite a la variable x para la funcion.
    
Ejemplo de ejecucion : 

    ./driver.py "f(x)= sin(x) " 2.2 2.37 4 
    
    Calcula el polinomio P_4 de Taylor de la funcion sin(x) (seno de x)  al rededor del p unto 2.2 y aproxima el valor de la funcion en 2.37
    
"""

def crea_funcion(s):
    lhs, rhs = s.split("=", 1)
    rhs = rhs.rstrip('; ')
    args = sympy.sympify(lhs).args
    f = sympy.sympify(rhs)
    def f_func(*passed_args):
        argdict = dict(zip(args, passed_args))
        result = f.subs(argdict)
        return float(result)
    return f_func
    


def crea_funcion_sim(s):
    lhs, rhs = s.split("=", 1)
    rhs = rhs.rstrip('; ')
    args = sympy.sympify(lhs).args
    f = sympy.sympify(rhs)
    return f


def taylor2(f,n):
    deltay=sympy.sympify("y-y0")
    tay=(sympy.diff(f,x,2)/sympy.factorial(2))*(deltay**(2))
    for i in range(n-2):
             
        tay = tay +(sympy.diff(f,x,i+3)/sympy.factorial(i+3))*(deltay**(i+3))

        
    
    return tay

def taylor(f,n):
    deltay=sympy.sympify("y-y0")
    tay=f
    for i in range(n):
        tay=tay+(sympy.diff(f,x,i+1)/sympy.factorial(i+1))*(deltay**(i+1))
    return tay















try :
    s=sys.argv[1]
    x0=float(sys.argv[2])
    x_val=float(sys.argv[3])
    n=int(sys.argv[4])
except :
    s=input("Introduce una exprecion de la forma completa en la variable x : g(x) = w(x)+ z(x) +... : ")
    x0=float(input("Introduce un punto x0 para formar la serie de s al rededor de el : "))
    x_val=float(input("Introduce un punto a evaluar tu aproximacion : ")) 
    n=int(input("Introduce grado maximo de la derivada en la serie de taylor: "))


f = crea_funcion_sim(s)


print("La funcion introducida es : ",f)


print("\n")
print("Se calculara el polinomio P_"+str(n)+" de Taylor de la funcion : ",f," al rededor del punto : ",x0, " y se evaluara en el punto : ",x_val )



x=sympy.Symbol('x')


deltay=sympy.sympify("y-y0")

w = taylor2(f,n)

#print(taylor(f,n))
#print(str(taylor(f,n).subs({'x':x0,'y0':x0}).evalf()))


print("\n")
print("Polinomio de Taylor P_"+str(n)+" calculado por el programa (evaluado en la variable y):")
print("\n")
print(str(w.subs({'x':x0,'y0':x0}).evalf()),' + '+str(sympy.diff(f,x).subs({'x':x0}).evalf()),'*(',deltay.subs({'y0':x0}),') + ',str(f.subs({'x':x0}).evalf()))
print("\n")

print("Polinomio de Taylor P_"+str(n)+" calculado usando directamente la libreria sympy (evaluado en la variable x) :")
print("\n")
print(sympy.series(f,x,x0=x0,n=n))
print("\n")


aprox=taylor(f,n).subs({'x':x0,'y0':x0,'y':x_val}).evalf()
valor=f.subs({'x':x_val}).evalf()
print("Valor aproximado : ", aprox)
print("Valor de python : ",valor)

print("Error absoluto (EA) : ", abs(aprox-valor))

if not valor ==0: 
    print("Error relativo (ER) : ", abs((aprox-valor)/valor))
    print("Error porcentual (e%) : ", 100*abs((aprox-valor)/valor))
#print(w.subs({'x':2.2,'y0':2.2}).evalf(),"+",f.subs({'x':2.2}))
