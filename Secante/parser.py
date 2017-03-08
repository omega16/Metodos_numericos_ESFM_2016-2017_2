#!/usr/bin/env python3




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
        
    
