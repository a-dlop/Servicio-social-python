# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:44:11 2019

@author: Daniel
"""

import numpy as np
elementos=['H',"He","Li","Be","B","N","C","O","F",
           "Ne","Na","Mg","Al","Si","P","S","Cl","Ar",
           "K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co",
           "Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
           "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh",
           "Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe",
           "Ir","Pt","Au","Begin","End"]


def iniciofin(datos, palabra):
    palabras=datos.split() #Divide los datos en un arreglo
    
    x=[ 0 for i in range(palabras.count(palabra)) ]#Crea arreglo  de 0s del tamaño de las palabras
    z=0
    for n in range(len(palabras)): #Inicializa for con longitud igual al numero palabras 
        if palabras[n]==palabra: #Si el elemento del arreglo es igual a la palabra utilizada se guarda la posición donde se encontro
            x[z]=n
            z=z+1
    return x
             
def nuevoarreglo(inicio,fin,palabras):#Crea arreglo del tamaño (fin-inicio),usado para dividir el arreglo en arreglos más pequeños que contengan las palabras Begin y End 
        x=[0 for i in range(fin-inicio)]    
        for i in range(fin-inicio):
           x[i]=palabras[inicio+i] 
        return x

        
def Contelem(datos):#Función para contar el número átomos en una molécula
   
    x=np.zeros(len(elementos)) #Crea arreglo del tamaño del diccionario de elementos
    for n in range(len(elementos)):
        x[n]=datos.count(elementos[n])#Cuenta las veces que aparece cada elemento del diccionario y añade la cantidad de veces que aparecio elemento a un arreglo
        if x[n]>0 and n<57:
            print(elementos[n]+ "= "+str(x[n]))#Imprime el valor obtenido
    y=0
    for n in range(len(x)-2): #-2 para eliminar el conteo de begin y end
       y=y+x[n]
    print("Total:"+str(y))        #Imprime el numero total de átomos en la molécula
    return x



def conteoimprimir(datos):
    palabra=datos.split()#Divide los datos en grupos
    inicio=iniciofin(datos,"Begin") #Del grupo de datos indica cuando inicia una molécula
    fin=iniciofin(datos,"End")#Indica cuando termina una molécula

    x=[nuevoarreglo(inicio[i],fin[i],palabra) for i in range(len(inicio))] #Crea un nuevo arreglo
    
    y=[i for i in range(len(inicio)+1)] #Almacena en un arreglo, cuantas veces apareció cada elemento
    for i in range(len(x)):                  
        y[i]=Contelem(x[i]) 
    
    y[len(x)]=palabra.count(elementos[57])   #Almacena cuantas moléculas fueron leidas
    print ("Moléculas contadas:") 
    print(y[len(x)])  
    return y    
        
f=open("elementos.txt","r")  #Lectura de archivo de texto con los datos
datos=f.read()
f.close()


z=conteoimprimir(datos)
print (z)