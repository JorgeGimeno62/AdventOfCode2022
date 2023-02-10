import pandas as pd
import string

#####EJERCICIO1#########

#######Sacamos serie de abecedario con su respectivo valor########
lista_alfabeto_conjunto =  list(string.ascii_lowercase) + list(string.ascii_uppercase)
diccionario_abecedario_completo = {}
valor=0

for letra in lista_alfabeto_conjunto:
    valor += 1
    diccionario_abecedario_completo[letra]=valor

dataframe = pd.read_csv("C:\\Users\\Jorge\\Python_Archivos\\AdventOfCode2022\\Dia3\\input.txt",delimiter='\t',names=['mochila'])
lista_de_mochilas =list(dataframe['mochila'])

####para mostrar las partes de la mochila en el dataframe
bolsillo_izquierdo = []
bolsillo_derecho = []
for mochila in lista_de_mochilas:
    contenido_mochila = len(mochila)
    bolsillo_izquierdo_contenido = mochila [0:int(abs(contenido_mochila/2))]
    bolsillo_izquierdo.append(bolsillo_izquierdo_contenido)
    bolsillo_derecho_contenido = mochila [int(abs(contenido_mochila/2)):len(mochila)]
    bolsillo_derecho.append(bolsillo_derecho_contenido)

###para mostrar la letra repetida    
dataframe_completo= dataframe.copy()
letraRepetida=[]
for contenidomochila in dataframe_completo['mochila']:

    bolsillo_izqdo = set(contenidomochila[0:int(abs(len(contenidomochila)/2))])
    bolsillo_drcho = set(contenidomochila[int(abs(len(contenidomochila)/2)):])
    interseccion =", ".join(bolsillo_izqdo & bolsillo_drcho)
    letraRepetida.append(interseccion)

###plasmar en el dataframe
dataframe_completo.insert(1,"Bolsillo Izquierdo", bolsillo_izquierdo)
dataframe_completo.insert(2,"Bolsillo Derecho",bolsillo_derecho)
dataframe_completo['letraRepetida']= letraRepetida

ValorLetraRepe = []
for letra in dataframe_completo['letraRepetida']:
        ValorLetraRepe.append(diccionario_abecedario_completo[letra])
dataframe_completo['ValorLetraRepe']= ValorLetraRepe


######EJERCICIO 2######## dividir en grupos de 3 mochilas
mochilasporgrupo = 3
lista_de_mochilas_agrupada = [lista_de_mochilas[i:i + mochilasporgrupo] for i in range(0,len(lista_de_mochilas),3)]
print(lista_de_mochilas_agrupada)

for grupo in lista_de_mochilas_agrupada:
    for mochila in grupo:
        mochila1 = set(mochila[0])
        mochila2 = set(mochila[1])
        mochila3 = set(mochila[2])
        interseccion=","

    