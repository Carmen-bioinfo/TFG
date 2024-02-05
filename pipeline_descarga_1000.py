# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:17:19 2022

@author: Windows
"""

import os

"""Esta pipeline descarga secuencias del SARS-CoV-2 en formato multifasta utilizando las e-utilities. 
Se le proporciona una lisa con las fechas finales de los meses a descargar.
Además, realiza el JSON para los k-meros de longitud 6 y 7, obtiene la lista con los k-meros con R=0 
y la media de los conteos en formato csv."""

# date_list = ["2020/05/31","2020/07/31", "2020/08/31", "2020/09/30", "2020/10/31", "2020/11/30", "2020/12/31",
#   "2021/01/31", "2021/02/28", "2021/03/31", "2021/04/30", "2021/05/31", "2021/06/30",
#   "2021/07/31", "2021/08/31", "2021/09/30", "2021/10/31","2021/11/30", "2021/12/31",
#   "2022/01/31", "2022/02/28", "2022/03/31", "2022/04/30", "2022/05/31", "2022/06/30",
#   "2022/07/31", "2022/08/31", "2022/09/30", "2020/06/30", "2020/04/30"] 

# date_list=["2022/10/31"]

date_list=["2022/11/30", "2022/12/31","2023/01/31", "2023/02/28", "2023/03/31", "2023/04/30", "2023/05/31", "2023/06/30","2023/07/31", "2023/08/31"]

for final_date in date_list: 
    date = final_date.split("/")
    date[2] = "01" 
    init_date = "/".join(date) #se construye la fecha inicial a partir de la final


    
    date_name = "%s_%s.txt" %(date[1], date[0])
    mf_name = "%s_%s_mf.txt" %(date[1], date[0])
    nombre_JSON_6=str("k6_"+ mf_name + '.json')
    nombre_JSON_7=str("k7_"+ mf_name + '.json')
    
    correcto_nombre_JSON_6=nombre_JSON_6.split(".") #Para que el nombre no incluya la extension ".json" en el nombre de la lista con R0
    correcto_nombre_JSON_7=nombre_JSON_7.split(".")
    
    R0_JSON_6=str("R0_"+correcto_nombre_JSON_6[0]+".txt")
    R0_JSON_7=str("R0_"+correcto_nombre_JSON_7[0]+".txt")
    
    nombre_string_6=str("csv_"+correcto_nombre_JSON_6[0]+".txt")
    nombre_string_7=str("csv_"+correcto_nombre_JSON_7[0]+".txt")
    
    os.system("esearch -db nuccore -query 'sars-cov-2' |efilter -mindate %s -maxdate %s |  efilter -query '28000:33000 [SLEN]'| efetch -format docsum | xtract -pattern DocumentSummary -element Id >ID.txt" %(init_date, final_date))
    
    os.system("python3 /home/carmen/programas_virus/rutas_ID.py ID.txt 1020 20") 
    
    os.system("cat salida1.txt salida2.txt salida3.txt salida4.txt salida5.txt salida6.txt salida7.txt salida8.txt salida9.txt salida10.txt salida11.txt salida12.txt salida13.txt salida14.txt salida15.txt salida16.txt salida17.txt salida18.txt salida19.txt salida20.txt salida21.txt salida22.txt salida23.txt salida24.txt salida25.txt salida26.txt salida27.txt salida28.txt salida29.txt salida30.txt salida31.txt salida32.txt salida33.txt salida34.txt salida35.txt salida36.txt salida37.txt salida38.txt salida39.txt salida40.txt salida41.txt salida42.txt salida43.txt salida44.txt salida45.txt salida46.txt salida47.txt salida48.txt salida49.txt salida50.txt salida51.txt  > %s" %(date_name))

    
    
    os.system("python3 /home/carmen/programas_virus/multifasta_correcto.py %s %s" %(date_name, mf_name))
    
    
    
    os.system("python3 /home/carmen/programas_virus/linux_primer_programa.py %s %i %s" %(mf_name, 6, nombre_JSON_6))
    
    os.system("python3 /home/carmen/programas_virus/linux_primer_programa.py %s %i %s" %(mf_name, 7, nombre_JSON_7))
    
    os.system("python3 /home/carmen/programas_virus/linux_tercer_programa_modifc.py %s %s" %(nombre_JSON_6, R0_JSON_6))
    
    os.system("python3 /home/carmen/programas_virus/linux_tercer_programa_modifc.py %s %s" %(nombre_JSON_7, R0_JSON_7))

    
    os.system("python3 /home/carmen/programas_virus/tabla_conteo_dsv.py %s %s" %(nombre_JSON_6, nombre_string_6))
    
    os.system("python3 /home/carmen/programas_virus/tabla_conteo_dsv.py %s %s" %(nombre_JSON_6, nombre_string_6))