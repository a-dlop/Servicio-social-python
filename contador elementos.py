# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:11:26 2019

@author: Daniel
"""
import numpy as np
def compare(word):
    res = 0
    for letter in word:
        res += elementos.get(letter, 0)
        # dict.get(key, defaultvalue)
    return res
elementos=["H ","He ","Li ","Be ","B ","N ","C ","O ","F ",
           "Ne ","Na ","Mg ","Al ","Si ","P ","S ","Cl ","Ar ",
           "K ","Ca ","Sc ","Ti ","V ","Cr ","Mn ","Fe ","Co ",
           "Ni ","Cu ","Zn ","Ga ","Ge ","As ","Se ","Br ","Kr ",
           "Rb ","Sr ","Y ","Zr ","Nb ","Mo ","Tc ","Ru ","Rh ",
           "Pd ","Ag ","Cd ","In ","Sn ","Sb ","Te ","I ","Xe ",
           "Ir ","Pt ","Au "]

def Contelem(datos):#Función para contar el número átomos en una molécula
    palabras=datos.split() #Transforma la cadena de texto en un arreglo con cada palabra
    x=np.zeros(len(elementos)) #Crea arreglo del tamaño del diccionario de elementos
    for n in range(len(elementos)):
        x[n]=datos.count(elementos[n])#Cuenta las veces que aparece cada elemento del diccionario y añade la cantidad de veces que aparecio elemento a un arreglo
        if x[n]>0:
            print(elementos[n]+ "= "+str(x[n]))#Imprime el valor obtenido
    y=0
    for n in range(len(x)): 
       y=y+x[n]
    print("Total:"+str(y))        #Imprime el numero total de átomos en la molécula
    return x

f=open("elemental.txt","r")  #Lectura de archivo de texto
datos=f.read()
f.close()
Contelem(datos)




"""palabras=datos.split() #Transforma la cadena de texto en un arreglo con cada palabra
print(palabras)
x=np.zeros(len(elementos))
print(x[0])
for n in range(len(elementos)):
    x[n]=datos.count(elementos[n])
    if x[n]>0:
        print(elementos[n]+ "= "+str(x[n]))
y=0
for n in range(len(x)): 
       y=y+x[n]
       
print(y)
"""