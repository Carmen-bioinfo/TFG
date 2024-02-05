# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:03:36 2021

@author: usuario
"""

import json
import sys
import pandas as pd 

input_path=sys.argv[1]
nombre_archivo=sys.argv[2]
# nombre_archivo1=input_path.split("/")
# nombre_archivo="R0_"+str(nombre_archivo1[6])


with open(input_path) as file:
    data = json.load(file)

def estadistica(input_path):
    kmeros={}
    list_valores=[] 
    virus_contador=0
    for virus in data:
        virus_contador=virus_contador + 1
        for key,value in data[virus].items():
            obs=value[2]
            esp=value[1]
            ratio=obs/esp
            
            if key in kmeros.keys(): #se le añade como valor el ratio
                kmeros[key].append(ratio) 
            
            else: #inicializamos la lista con el ratio obs-esp
                list_valores.append(ratio)
                kmeros[key]=list_valores
                list_valores=[] 
       
    for key, value in kmeros.items(): #añade los ceros para completar según el número de virus
        while len(value)< virus_contador:
            kmeros[key].append(0)
             
              
    tabla1=pd.DataFrame(kmeros)
    
    
    
    tabla1.loc[virus_contador]=tabla1[:].median() 
    
    tabla1.loc[virus_contador+1]=tabla1[:].mean()
    
    tabla1.loc[virus_contador+2]=tabla1[:].min()
    
    tabla1.loc[virus_contador+3]=tabla1[:].max()
    
    tabla1.loc[virus_contador+4]=tabla1[:].var() 
    
    tabla1.loc[virus_contador+5]=tabla1[:].quantile(0.10)
    
    tabla1.loc[virus_contador+6]=tabla1[:].quantile(0.25)
    
    tabla1.loc[virus_contador+7]=tabla1[:].quantile(0.75) 
    
    tabla1.loc[virus_contador+8]=tabla1[:].quantile(0.90)
    
    
    tabla2=tabla1.iloc[virus_contador:virus_contador+9, :] 
    
    tabla2.index = ["median", "mean", "min", "max","var", "p10", "p25", "p75", "p90"]
    
    tabla3=pd.DataFrame.transpose(tabla2)
     
    return tabla3

tabla_estadistica=estadistica(input_path)

# tabla_estadistica.to_string("tabla_estadistica.txt")

def Orden_menor(tabla_estadistica):
    orden_menor=tabla_estadistica.sort_values("mean")
    # seleccion=orden_menor.iloc[0:249]
    reqd_index = tabla_estadistica.query('mean == 0.00000').index.tolist() 
    # reqd_index=seleccion.index.tolist() 
    
    
    
    # abajo he puesto reqd_index porque quiero la lista de los que tienen 0, pero si quisiera la tabla
    # pondría orden_menor
    return reqd_index

def Orden_mayor(tabla_estadistica):
    orden_mayor=tabla_estadistica.sort_values("mean", ascending=False)
    seleccion=orden_mayor.iloc[0:320]
    # reqd_index=seleccion.index.tolist()
    # print(reqd_index)
    return orden_mayor

orden_menor=Orden_menor(tabla_estadistica)

f = open(nombre_archivo,'w')

for x in orden_menor:
    f.write(str(x) + "\n")
f.close()

# orden_menor.to_string("orden_menor_tabla_estadistica.txt")
# orden_menor.to_csv("orden_menor_csv.csv")

# orden_mayor=Orden_mayor(tabla_estadistica)
# orden_mayor.to_string("orden_mayor_tabla_estadistica.txt")
# orden_mayor.to_csv("orden_mayor_csv.csv") 
