# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:23:14 2022

@author: Windows
"""

import numpy as np
import sys
import os

lista_ID=sys.argv[1]
n=int(sys.argv[2]) #numero de secuencias que se quiere coger
m=int(sys.argv[3]) #divisiones con las que se quiere trabajar


def eleccion_azar(lista_ID, n):
   with open(lista_ID, "r") as ifile:
       lines=ifile.readlines()
   lista_ID=[]
   for x in lines:
       lista_ID.append(x.strip())    
   seleccion=np.random.choice(lista_ID, n, replace=False)    
   select2=seleccion.tolist()
   return select2

def poner_en_lista(test_list,m):
    output=[test_list[i:i + m] for i in range(0, len(test_list), m)]
    return output

lista_comandos=[]
def escribe_comando(output):

    comando="efetch -db nuccore -id "
    salida=0
    for x in output:
        añadir=",".join(x)
        comando+=añadir 
        comando+=" -format fasta >" 
        salida+=1
        string_salida="salida"+str(salida)+".txt" +"\n"
        comando+=string_salida

        # f.write(comando)
        lista_comandos.append(comando)
        añadir=""
        comando="efetch -db nuccore -id "
             
    return lista_comandos
    
seleccion=eleccion_azar(lista_ID, n)

combinacion=poner_en_lista(seleccion, m)

command_list=escribe_comando(combinacion)

for l in command_list:
    os.system(l)

# f=open("comandos", "w")
# comando=escribe_comando(combinacion)
# f.close()

