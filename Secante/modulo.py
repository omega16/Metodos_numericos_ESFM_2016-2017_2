#!/usr/bin/env python3

from parser import *
import sys
import numpy as np


rayas=True


def funcion_clase(x,eps):
    if type(x)==str :
        return "Error, derivada no definida"
    
    
    if type(x**(7/8))==type((-1)**(1/2)):
        return "Error, numero complejo como resultado"
        
    if (not np.abs(x**2 -3*x  -3)<eps )  and (not np.abs(np.cos(x)) < eps ) :
   
        return (np.sin(x)* (x**3) )- np.log(np.abs(np.cos(x))) - x**(7/8) - 1/(x**2 -3*x -3) -24.8
            
            
    else: 
            return "Error, derivada no definida"
    
    
def deriva_funcion_clase(x,eps):
  
    if (not np.abs(x)<eps) and (not np.abs(x**2 -3*x  -3)<eps )  and ( type(x**(-1/8)!=type((-1)**(1/2)))):
        
        
        
        if np.cos(x)>0 :
    
            return ( np.cos(x)* (x**3) ) + ( np.sin(x)*(3* (x**2)) ) + ( np.sin(x)/np.cos(x) ) - ( (7/8) * x**(-1/8) ) + ( (2*x -3)/ ((x**2 -3*x -3)**2) ) - 24.8

        elif np.cos(x)<0 : 
    
            return ( np.cos(x)* (x**3) ) + ( np.sin(x)*(3* (x**2)) ) - ( np.sin(x)/np.cos(x) ) - ( (7/8) * x**(-1/8) ) + ( (2*x -3)/ ((x**2 -3*x -3)**2) ) - 24.8
         
        else: 
            
            return "Error, derivada no definida"
            
       
            
    else: 
            return "Error, derivada no definida"




def newton_raphson_step(f,fder,x,eps):

    try :
        return x - (f(x,eps)/fder(x,eps))
    except :
        return "Detenido por un problema con la funcion o la derivada"


def secante(f,fder,x1,x2,eps):
    try: 
        return x1-(f(x1,eps)*(x1-x2)/(f(x1,eps)-f(x2,eps))
    except:
        return "Detenido por un problema al evaluar el metodo de la secante"    
    


def method_intervalo(f,fder,x0,tol,eps):
    x=[]
    x.append(x0)
    for i in range(tol):

        x.append(newton_raphson_step(f,fder,x[-1],eps))
       
        if (type(x[-1])==str):
            break
        if (np.abs(f(x[-1],eps))< eps) :
            break
        

        
    
    return x




def method(f,fder,a,b,tol,eps,itera):
    
    t=np.linspace(a,b,itera+1)
    raices=[]
    for i in range(itera):
        raices.append(method_intervalo(f,fder,t[i+1],tol,eps))
    
    return t,raices





def depura(lista):
    return sorted(dict.fromkeys(lista).keys())




def imprimir(ruta,raices,t,f,eps,a,b):
    global rayas
    
    arch=open(ruta,'a')
    arch.write("|  {0:10s}  |  {1:.22s}  |  {2:.22s}  |  {3:.22s}  |  {4:.22s}  |".format('k', 'x_k', 'f(x_k)', '|f(x_k)|', '|x_k - x_k+1|'))
    for i in range(len(raices)):
     #print ("------------------------------aproximacion del intervalo (%f,%f) ---------------------------------------"%(t[i],t[i+1]))
     #print("----------------------------------------------------------------------------------------------------------------------------")
     arch.write("----------------------------------------------------------------------------------------------------------------------------")
     
     if rayas:
        #print("|  {0:10s}  |  {1:.22s}  |  {2:.22s}  |  {3:.22s}  |  {4:.22s}  |".format('k', 'x_k', 'f(x_k)', '|f(x_k)|', '|x_k - x_k+1|'))
        #arch.write("|  {0:10s}  |  {1:.22s}  |  {2:.22s}  |  {3:.22s}  |  {4:.22s}  |".format('k', 'x_k', 'f(x_k)', '|f(x_k)|', '|x_k - x_k+1|'))
        arch.write('\n')
     else :
        #print("  {0:10s}    {1:.22s}    {2:.22s}    {3:.22s}    {4:.22s}  ".format('k', 'x_k', 'f(x_k)', '|f(x_k)|', '|x_k - x_k+1|'))
        #arhc.write("  {0:10s}    {1:.22s}    {2:.22s}    {3:.22s}    {4:.22s}  ".format('k', 'x_k', 'f(x_k)', '|f(x_k)|', '|x_k - x_k+1|'))
        arch.write('\n')
     #print("%s \t | \t %16s \t | \t  %16s \t | \t  %16s \t | \t %16s"%('k','x_k','f(x_k)','|f(x_k)|','|x_k - x_k+1|'))
     
     
     
     
     for j in range (len(raices[i])):
     
        if not type(raices[i][-1])==str and j<len(raices[i])-1:
            
            if rayas:
            
                #print("|  {0:10d}  |  {1:.22f}  |  {2:.22f}  |  {3:.22f}  |  {4:.22f}  |".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps)), np.abs(raices[i][j]-raices[i][j+1])))
                
                arch.write("|  {0:10d}  |  {1:.22f}  |  {2:.22f}  |  {3:.22f}  |  {4:.22f}  |".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps)), np.abs(raices[i][j]-raices[i][j+1])))
                
                arch.write('\n')
                
            else:
                #print("  {0:10d}    {1:.22f}    {2:.22f}    {3:.22f}    {4:.22f}  ".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps)), np.abs(raices[i][j]-raices[i][j+1])))
                
                
                arch.write("  {0:10d}    {1:.22f}    {2:.22f}    {3:.22f}    {4:.22f}  ".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps)), np.abs(raices[i][j]-raices[i][j+1])))
                
                arch.write('\n')
                
            #print("%d \t | \t %.16f \t | \t %.16f \t | \t %.16f \t | \t %.16f "%(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps)), np.abs(raices[i][j]-raices[i][j+1]) ))
        elif not type(raices[i][-1])==str and j==len(raices[i])-1 :
            
            if rayas:
            
                #print("|  {0:10d}  |  {1:.22f}  |  {2:.22f}  |  {3:.22f}  |".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps))))
                
                arch.write("|  {0:10d}  |  {1:.22f}  |  {2:.22f}  |  {3:.22f}  |".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps))))
                
                arch.write('\n')
                
                
            else : 
                #print("  {0:10d}    {1:.22f}    {2:.22f}    {3:.22f}  ".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps))))
                
                arch.write("  {0:10d}    {1:.22f}    {2:.22f}    {3:.22f}  ".format(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps))))
                
                arch.write('\n')
            
            #print("%d \t | \t %.16f \t | \t %.16f \t | \t %.16f \t     |  "%(j,  raices[i][j],  f(raices[i][j],eps),  np.abs(f(raices[i][j],eps)) ))
    
    aux=[y[-1] for y in raices if type(y[-1])!=str ]
    
    aux=depura(aux)
    
    aux2=[]
    for i in range(len(aux)):
        if i<len(aux)-1:
            if np.abs(aux[i]-aux[i+1])>eps:
                aux2.append(aux[i])
    aux2.append(aux[-1])
    
    
    arch.write("\n \n \n Numero de raices encontradas: {0:10d} \n \n Raices:  ".format(len(aux2)))
 
    for i in aux2 : 
        arch.write("\n {0:.22f} \n".format(i))
        
    arch.close()
    
    print("Encontradas {0:10d} en el intervalo ({1:.22f},{2:.22f})".format(len(aux2),a,b)) 
    
    
    



def testmethod(f,fder):
    global rayas
    try : 
        tol = int(sys.argv[1])
        eps = float(sys.argv[2])
        ex_izq = float(sys.argv[3])
        ex_der = float(sys.argv[4])
        itera = int(sys.argv[5])
        rayas = bool(int(sys.argv[6]))
        ruta = sys.argv[7]
    
    
    
    except:

        print("No se an recibido argumentos o hubo un error al cargar los argumentos ")

        param_nombres   =   [     "Tolerancia (max iter) " ,      "Epsilon",      "Extremo izquierdo de intervalo" , "Extremo derecho de intervalo"      ,     "Numero de diviciones"      ,"Activar lineas de tabla en salida (1/0)" ,"Ruta de salida completa (/home/user/.../archivo.txt)"]

        param_tipos     =   [      int                     ,       float   ,        float                          ,      float                           ,       int                         ,             bool                         ,              str                                     ]

        tol,eps,ex_izq,ex_der,itera,rayas,ruta=inicio(param_nombres,param_tipos)
        
    


    inter,raices=method(f,fder,ex_izq,ex_der,tol,eps,itera)
    imprimir(ruta,raices,inter,f,eps,ex_izq,ex_der)





