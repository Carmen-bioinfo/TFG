# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 17:15:48 2023

@author: Windows
"""
import random
import sys

#input_path=r"C:\Users\Windows\Desktop\CARMEN\BIOQUÍMICA\TRABAJO DE FIN DE GRADO\PROGRAMAS\seqprueba_aleatorizar.txt"
input_path=sys.argv[1]
nombre_aleatorizado=str(sys.argv[2])


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

def aleatorizar(dict1):
    for clave,valor in dict1.items():
        s=valor
        aleatorio=''.join(random.sample(s,len(s)))
        dict1[clave]=aleatorio
        
    return dict1
def multifasta(dict1):
    for clave,valor in dict1.items():
        f.write(">" + clave +"\n" + valor + "\n")

variable=sequences(input_path)
variable_aleatoria=aleatorizar(variable)
f = open(nombre_aleatorizado, "w")
Multifasta_aleatorio=multifasta(variable_aleatoria)
f.close()
