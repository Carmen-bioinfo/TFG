# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:27:43 2022

@author: Windows
"""
import sys
import numpy as np

input_path=sys.argv[1]
n=int(sys.argv[2])
nombrearchivo=str(sys.argv[3])

def sequences (input_path):
    variable="" #guarda el nombre de los virus
    secuencia="" #almacena las secuencias
    nombre_old="" #para poner correctamente la clave del virus
    dict1={} 

    """lee el multifasta y lo guarda en un diccionario 
                (clave: virus- valor: secuencia)"""
                
    with open(input_path, "r") as ifile:
        lines=ifile.readlines()    
    for l in lines:
        if l.startswith(">"):
            variable=l.rstrip()
            lista_fraccionada=variable.split(">") #obtener el nombre del virus sin >
            nombre_virus=lista_fraccionada[1]
                        
            if len(secuencia) > 0: 
                dict1[nombre_old]=secuencia
            
            nombre_old=nombre_virus
            secuencia=""
        
        else:
            secuencia=secuencia + l.rstrip().upper()
        
        dict1[nombre_old]=secuencia 
        
        for virus, secuencia in list(dict1.items()):
            if "A" and "T" and "G" and "C" in secuencia:
                continue
            else:
                dict1.pop(virus)

    return dict1

def secuencias_azar(dict1, n):
    lista_de_claves=[]
    for key in dict1.keys():
        lista_de_claves.append(key)
    seleccion=np.random.choice(lista_de_claves, n, replace=False)    
    select2=seleccion.tolist()
    return select2

def seleccion_de_secuencias(dict1, select2):
    new_dict={}
    for key, value in list(dict1.items()):
        for s in select2:
            if s == key:
                new_dict[key]=value
            else:
                continue
    return new_dict 

f=open(nombrearchivo, "w")
def guardar_mf(new_dict):
    for key,value in new_dict.items():
        f.write(">"+key+"\n")
        f.write(value+"\n")

    return new_dict
        


Secuencias=sequences(input_path)
Seleccion_azar=secuencias_azar(Secuencias, n)
Seleccionar=seleccion_de_secuencias(Secuencias, Seleccion_azar)     
guardar_mf=guardar_mf(Seleccionar)         
f.close()        
        
        
        