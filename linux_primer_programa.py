# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 12:53:47 2021

@author: usuario
"""
import sys 
import json 
import itertools

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
    return dict1
         
def Combinations(n):
    """nos devuelve una lista con las posibles 
    combinaciones de letras del ADN de longitud n"""
    
    x = ["A","G","C","T"]
    combinations=[] 
    lista_p=[]
    for p in itertools.product(x, repeat=n):
        lista_p=list(p)
        combinations.append("".join(lista_p))
    return combinations    
                      
def counts (dict1,n): 
    conteo = {} #pares clave-valor
    total_counts= {}
    nucleotidos=("A", "G", "C", "T")
    """guarda el diccionario con los conteos"""
    for clave in dict1:
        valor = dict1[clave]
        for i,s in enumerate(valor):
            posicion_actual=valor[i:i+n] 
            if len(posicion_actual)<n:
                continue
            if posicion_actual in conteo.keys() and len(posicion_actual)==n:
                conteo[posicion_actual]+=1
            else:
                conteo[posicion_actual]=1
        total_counts[clave]=conteo
        conteo={}
        
    for virus, palabras in list(total_counts.items()): 
        for letras in list(palabras.keys()):
            for x in letras:
                if x in nucleotidos:
                    continue
                else:
                    if letras in palabras:
                        palabras.pop(letras)
                    else:
                        continue
    
    for virus, palabras in list(total_counts.items()):
        for key in list(palabras.keys()):
            for c in combinations:
                if c in palabras.keys():
                    continue
                else:
                    palabras[c]=0
            
    return total_counts
        

def normalize(sequences,total_counts):
    """conteo, freq esperada y freq observada de los datos anteriores"""
    lista=[]#guardará todos los datos correspondientes
    #----lo que necesito para la frecuencia esperada
    occurrences1={} #guarda la frecuencia esperada 
    occurrences2={} #guarda los conteos
    #-----lo que necesito para la frecuencia observada
    freq_obs=""
    #-----lo que necestio para la ratio
    ratio=""
    
    for clave,valor in sequences.items(): #nucleótido:prob en cada secuencia para cada virus
        freqA1=valor.count("A")
        freqC1=valor.count("C")
        freqG1=valor.count("G")
        freqT1=valor.count("T")
        
        sum_nucleotidos=int(freqA1 + freqC1 + freqG1 + freqT1)
        
        freqA2=freqA1/sum_nucleotidos
        occurrences2["A"]=freqA2 #añadir el valor (freq) a la clave (letra)
        
        freqC2=freqC1/sum_nucleotidos
        occurrences2["C"]=freqC2
        
       
        freqG2=freqG1/sum_nucleotidos
        occurrences2["G"]=freqG2
        
       
        freqT2=freqT1/sum_nucleotidos
        occurrences2["T"]=freqT2
        
        occurrences2["longitud"]=sum_nucleotidos
        
        occurrences1[clave]=occurrences2 #asignar el diccionario al nombre del virus
        occurrences2={}
    
    
    for k,v in total_counts.items():
        if k in total_counts.keys() and k in sequences.keys() and k in occurrences1.keys():
            # longitud=len(sequences[k]) #longitud de las secuencias
            diccionario=occurrences1[k] 
            
            freq_esp=float(1)
            for x,y in v.items():
                lista.append(y) #conteo de la secuencia actual
                
                for i in x:
                    if i in diccionario.keys():
                        freq_esp=freq_esp*diccionario[i] 
                        
                lista.append(freq_esp)
            
                freq_obs=y/sum_nucleotidos #cálculo frecuencia observada
                lista.append(freq_obs)
                ratio=freq_obs/freq_esp
                lista.append(ratio)
                
                v[x]=lista #añadimos la lista como clave
                            #vaciamos las variables para la siguiente iteración
                lista=[]
                freq_esp=float(1)
                freq_obs=""
                ratio=""
                

    return total_counts
    


#secuencias almacenadas en un diccionario
sequences=sequences(input_path) 

combinations=Combinations(n)     

total_counts=counts(sequences,n)

normCounts = normalize(sequences,total_counts)

with open(nombrearchivo, 'w') as file:
    json.dump(normCounts, file, indent=4)
    
