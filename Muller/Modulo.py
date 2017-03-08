#!/usr/bin/env python3

import sympy
import numpy as np

x = sympy.Symbol('x')
eps = 1e-10
tol = 100
x0=0
x1=0
x2=0
p = []
pol=sympy.Poly('x',x)

def lee_pol():
    a = input("Introduce un polinomio de una variable en la forma : a_n*x**(n-1)  + a_(n-1) * x**(n-2) +... : ")
    b = input("Introduce la variable en la que escribiste tu polinomio (el ejemplo usa: 'x')")
    
    print("El polinomio introducido es: ")
    
    global x
        
    x=sympy.Symbol(b)
    f=sympy.Poly(a,x)

    print(f)
    
    return f
    

def puntos():
    x0 = float(input("Introduce x0 : "))
    x1 = float(input("Introduce x1 : "))
    x2 = float(input("Introduce x2 : "))
    print("Parametros introducidos : x0 = {0:0.16f} , x1 = {1:0.16f} , x2 = {2:0.16f} ".format(x0,x1,x2))
    return x0,x1,x2


def error():
    global eps 
    eps = float(input("Introduce un Epsilon para el error : "))
    print("Epsilon establecido como : {0:0.20f}".format(eps))
    
    global tol
    tol = int(input("Introduce el maximo numero de iteraciones (tol) : "))
    print("Tolerancia establecida como : {0:6d}".format(tol))
    

def comprobar():
    a=input(" ¿Es lo anterior correcto? (y/n)") 
    if a=='y':
        return 1
    else :
        return 0 
    




def lee():
    global pol
    pol = lee_pol()
    global x0,x1,x2
    x0,x1,x2 = puntos()
    error()
    
    if comprobar () == 1:
        global p
        p = [x0,x1,x2]

      
    else :
        leer()






def delta1(x0,x1,f):
    return (f(x1)-f(x0))/(x1-x0)

def delta2(x0,x1,x2,f):
    return (delta1(x1,x2,f)-delta1(x0,x1,f))/(x2-x0)

def deter(a,b,c,f):
    w=complex(np.sqrt(b**2 -(4*a*c) +0J ))
    if abs(b+w)<abs(b-w):
        return -w
    else : 
        return w


def paso(x0,x1,x2,f):
   if x0!=x1 or x2!=x0 :
    a=complex(delta2(x0,x1,x2,f))
    b=complex(delta1(x0,x2,f)+delta1(x1,x2,f)-delta1(x0,x1,f))
    c=complex(f(x2))
    
    return x2-(2*c/(b+ deter(a,b,c,f )  ))
   else :
    return("PAron")
    
    
"""def delta1(x0,x1,f):
    return complex((f(x1)-f(x0))/(x1-x0))
    
  
    
def delta2(x0,x1,x2,f):
    return complex((delta1(x1,x2,f)-delta1(x0,x1,f))/(x2-x0))



def muller_coeff(x0,x1,x2,f) :

    if x1==x0 or x2==x0:
        return "Error div por cero","1","2"
    else : 
        

        return delta2(x0,x1,x2,f),delta1(x0,x2,f)+delta1(x1,x2,f)-delta1(x0,x1,f),f(x2)







def deter(b,coeff):

    coeff = np.sqrt(coeff + 0J)
    
    if abs(-b +  coeff) < abs(-b - coeff) :
        print("menos",coeff)
        return b -coeff
        
    else:
        print("mas",coeff)
        return b +coeff    
       





def muller_pass(y0,y1,y2,pol):

    a,b,c=muller_coeff(y0,y1,y2,pol)  

    if type(a)==str:
        return "Error de div por cero"

    coeff=complex((b**2)-(4*a*c))

    if a != 0: 
        return complex(y2 -(2*c/(deter(b,coeff)  )  ))
        
    else : 
        return "Error, tal vez converge"
        



"""

def iterar(pol):
      global x0,x1,x2,eps,tol
      z=[x0,x1,x2]
      w=0
      for i in range(tol):
          z.append(paso(z[0+i],z[1+i],z[2+i],pol))
          

          if type(z[-1])==str:
            break  
          elif abs(complex( pol(z[-1]).evalf() ))<eps :
            w=i
            break

      return z[:-1],w


def driv_man():
    lee()
    global pol
    sol,itera=iterar(pol)
    print("Las soluciones son:")
    for i in range(len(sol)): 
        print(  "\n {0:.16f},{1:0.16f}\n ".format(sol[i],abs(complex(pol(sol[i]))) )  )
    print("Iteraciones : {0:4d}".format(itera))
    global eps
    print("Epsilon : {0:0.16f}".format(eps))
    print("Solucion final {0:.16f},{1:0.16f}".format(sol[-1],abs(complex(pol(sol[-1])))))


    
def driv(y0,y1,y2,f,y,eps1,tol1):
    global x0,x1,x2,pol,x,eps,tol
    x0,x1,x2,x,eps,tol=[y0,y1,y2,sympy.Symbol(y),eps1,tol1]
    pol=sympy.Poly(f,x)
    sol,itera=iterar(pol)
    print("Las soluciones son:")
    print("\n {0:35s}     |     {1:16s} \n".format("X_k","|f(X_k)|"))
    for i in range(len(sol)): 
        print(  "\n {0:.16f}     |     {1:0.16f}\n ".format(sol[i],abs(complex(pol(sol[i]))) )  )
    print("Iteraciones : {0:4d}".format(itera))
    global eps
    print("Epsilon : {0:0.16f}".format(eps))
    print("Solucion final {0:.16f}".format(sol[-1]))
    print("Modulo de la funcion en la solucion : ",abs(complex(pol(sol[-1]))))
