#!/usr/bin/env python3

import sympy

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




def inicio(nombres,tipos):
    parametros=[]
    for i in range(len(nombres)):
    
        if tipos[i]!='funcion':
                
            if tipos[i]==bool:
                parametros.append(bool(int(input("Por favor introdusca "+nombres[i]+" : "))))
            else:    
                parametros.append(tipos[i](input("Por favor introdusca "+nombres[i]+" : ")))
        
        else :
            
            parametros.append(input("Por favor introdusca "+nombres[i]+" : "))
    
    return parametros
        
    
