# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:57:22 2020

@author: Steven Rubio

Vislualización de datos para ncovgt2020
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
import json
import numpy as np

#Funciones

# Función para obtener los casos diarios Regionales
def DiarioR(Lista):
        # ----------
    # Entradas:
    # Lista      = Lista con la cantidad de casos Regionales
    # ----------
    # Salidas:
    # NuevaLista = Lista con el número de casos por día
    # ----------
    NuevaLista = []
    for i in range(1,len(Lista)):
        val = Lista[i]-Lista[i-1]
        NuevaLista.append(val)
        
    return NuevaLista

GRAF = False
#Modifico los fonts del plot
#Opciones con: print(plt.style.available)
plt.style.use('ggplot')

#Cambio de directorio
os.chdir('../data')

#Lectura del Archivo con los datos
dfs = pd.read_csv('resumen_todos.csv')

#VExtracción de Variables
L_fecha  = dfs['fecha']
L_confrs = dfs['confirmados']
L_recups = dfs['recuperados']
L_fallds = dfs['fallecidos']
L_activs = dfs['activos']
L_pruebs = dfs['pruebas']
dias_Caso1 = range(len(L_fecha))

#Ultimo día actualizado
fechaH = L_fecha[len(L_fecha)-1]
fechaH = fechaH[:10]

#--------------------------///----------------------------------------
if(GRAF):
    #Creacion del plot 1. 
    #Casos Acumulados
    fig1 , ax = plt.subplots(1,1,figsize=(12, 8))
    
    ax.plot(dias_Caso1, L_confrs, linestyle='-', marker='v', label='Casos Confirmados'  ,color='#2076FB')
    ax.plot(dias_Caso1, L_recups, linestyle='-', marker='<', label='Casos Recuperados'  ,color='#0DBB10')
    ax.plot(dias_Caso1, L_fallds, linestyle='-', marker='>', label='Casos Fallecidos'   ,color='#C725E1')
    ax.plot(dias_Caso1, L_activs, linestyle='-', marker='^', label='Casos Activos'      ,color='#FA6311')
    
    #Nombre
    ax.set_title('Evolución Covid-19 GT '+fechaH)
    ax.set(ylabel='Total de Casos',xlabel='Días a partir del caso 1')
    
    # Add a legend
    ax.legend()
    plt.legend(loc='upper left')
    
    #Show
    plt.show()
    
    #Save
    #Cambio de directorio
    os.chdir('../imgs')
    fig1.savefig("Casos_Acumulados.png")

#--------------------------///----------------------------------------
if(GRAF):
    #Creacion del plot 2
    #Casos Diarios
    fig1 , ax = plt.subplots(1,1,figsize=(12, 8))
            
    ax.plot(dias_Caso1[:-1], DiarioR(L_confrs), linestyle='-', marker='.', label='Casos Confirmados'  ,color='#2076FB')
    ax.plot(dias_Caso1[:-1], DiarioR(L_recups), linestyle='-', marker='*', label='Casos Recuperados'  ,color='#0DBB10')
    ax.plot(dias_Caso1[:-1], DiarioR(L_fallds), linestyle='-', marker=',', label='Casos Fallecidos'   ,color='#C725E1')
    ax.plot(dias_Caso1[:-1],  DiarioR(L_activs), linestyle='-', marker='^', label='Casos Activos'      ,color='#FA6311')
    
    #Nombre
    ax.set_title('Evolución casos diarios Covid-19 GT '+fechaH)
    ax.set(ylabel='Total de Casos',xlabel='Días a partir del caso 1')
    
    # Add a legend
    ax.legend()
    plt.legend(loc='upper left')
    
    #Show
    plt.show()
    
    #Save
    #Cambio de directorio
    os.chdir('../imgs')
    fig1.savefig("Casos_Diarios.png")
    
#--------------------------///----------------------------------------
if(GRAF):
    #Creacion del plot 3. 
    #Pruebas Acumuladas y Diarias
    fig1 , ax = plt.subplots(1,1,figsize=(12, 8))
    
    #Cambio de step en la gráfica
    plt.xticks(np.arange(0,100,5))
    
    ax.bar(dias_Caso1[:-1], DiarioR(L_pruebs),width = 0.75, label='Pruebas Diarias'  ,color='#2EB007')
    ax.semilogy(dias_Caso1, L_pruebs, label='Pruebas Acumuladas' ,color='#509EAA')
    
    #Nombre
    ax.set_title('Datos Pruebas Realizadas Covid-19 GT '+fechaH)
    ax.set(ylabel='Total de Pruebas',xlabel='Días a partir del caso 1')
    
    # Add a legend
    ax.legend()
    ax.grid(True)
    plt.legend(loc='upper left')
    
    #Show
    plt.show()
    
    #Save
    #Cambio de directorio
    os.chdir('../imgs')
    fig1.savefig("Resumen_Pruebas_semilogy.png")
#--------------------------///----------------------------------------

if(GRAF):
    #Creacion del plot 4 
    #Pruebas Diarias y confirmados Diarios
    fig1 , ax = plt.subplots(1,1,figsize=(12, 8))
   
    #Data necesaria
    D_c = DiarioR(L_confrs)
    D_p = DiarioR(L_pruebs)
    R_cp = []
    #Validador para imprimir en consola
    Val = True
    
    for i in range(len(D_p)):
        #Reporte cuando no se encuentran pruebas Diarias
        if(D_p[i] == 0):
            R_cp.append(0)
            if(Val): 
                print("No se reportaron Pruebas estos días: ")
                Val = False
            print(L_fecha[i+1][:10])
        else:
            R_cp.append(100*D_c[i]/D_p[i])  
        
        
    plt.stackplot(dias_Caso1[:-1],R_cp, labels=['Razón confirmados/pruebas'], colors="#2ecc71", alpha=0.4 )
    plt.legend(loc='upper left')   
    #Nombre
    ax.set_title('Casos confirmados vs Pruebas diarias Covid-19 GT '+fechaH)
    ax.set(ylabel='Porcentaje',xlabel='Días a partir del caso 1')
    
    # Add a legend
    ax.legend()
    plt.legend(loc='upper left')
    
    #Show
    plt.show()
    
    #Save
    #Cambio de directorio
    os.chdir('../imgs')
    fig1.savefig("Razon_confirmados_pruebas_diario.png")  
    
    
#--------------------------///----------------------------------------    
if(GRAF):
    #Creacion del plot 5
    #Pruebas Diarias y negativos
    fig1 , ax = plt.subplots(1,1,figsize=(12, 8))
   
    #Data necesaria
    D_p = DiarioR(L_pruebs)
    #Validador para imprimir en consola
    Val = True
    R_cp = []
    
    for i in range(len(D_p)):
        #Reporte cuando no se encuentran pruebas Diarias
        if(D_p[i] == 0):
            R_cp.append(0)
            if(Val): 
                print("No se reportaron Pruebas estos días: ")
                Val = False
            print(L_fecha[i+1][:10])
        else:
            var = (L_pruebs[i+1]-L_confrs[i+1])/D_p[i]
            R_cp.append(var)  
        
        
    plt.stackplot(dias_Caso1[:-1],R_cp, colors="#0C4FC6", alpha=0.4 )
    plt.legend(loc='upper left')   
    #Nombre
    ax.set_title('Casos negativos vs Pruebas diarias Covid-19 GT '+fechaH)
    ax.set(ylabel='Razón',xlabel='Días a partir del caso 1')
    
    # Add a legend
    #ax.legend()
    #plt.legend(loc='upper left')
    
    #Show
    plt.show()
    
    #Save
    #Cambio de directorio
    os.chdir('../imgs')
    fig1.savefig("Razon_negativos_pruebas_diario.png")  
    
    
#--------------------------///---------------------------------------- 
if(True):
    #Creacion del plot 6. 
    #Casos Acumulados
    fig1 , ax = plt.subplots(1,1,figsize=(12, 8))
    
    #Plot con porcentajes
    YP1 = []
    YP2 = []
    YP3 = []
    XP = []
    for i in range(len(L_activs)):
        a = L_activs[i]+L_fallds[i]+L_recups[i]
        if(a!= 0):
            YP1.append(100*L_activs[i]/a)
            YP2.append(100*L_recups[i]/a)
            YP3.append(100*L_fallds[i]/a)
            XP.append(i)
          
    YP = (YP3,YP2,YP1)  
    #Promedios
    # Paleta de colores
    pal = ["#9b59b6", "#DAF7A6", "#1E98C0"]
    plt.stackplot(XP, YP, labels=['Casos Fallecidos       ('+str(round(YP3[-1],2))+'%)','Casos Recuperados  ('+str(round(YP2[-1],2))+'%)','Casos Activos           ('+str(round(YP1[-1],2))+'%)'], colors=pal, alpha=0.7)
    plt.legend(loc='upper left')

    #Nombre
    ax.set_title('Evolución Casos Covid-19 GT '+fechaH)
    ax.set(ylabel='Porcentaje',xlabel='Días a partir del caso 1')
    
    # Add a legend
    ax.legend()
    plt.legend(loc='upper left')
    
    #Show
    plt.show()
    
    #Save
    #Cambio de directorio
    os.chdir('../imgs')
    fig1.savefig("Evolucion_Porcentaje_Casos.png")

#--------------------------///---------------------------------------- 
'''
if(False):
    #Creacion del plot 6
    fig2 , ax = plt.subplots(1,1)
    
    #Cambio de directorio
    os.chdir('../data/record')
    x = os.listdir()
    
    #Variables
    os.chdir(x[-1])
    
    L_confrs_d = []
    L_recups_d = []
    L_fallds_d = []
    L_activs_d = []
    
    with open('resumen_todos.json') as f:
        data = json.load(f)
        for i in data['features']:
            if(i['attributes']['Estado'] == 'Activo'): 
                x1 = i['attributes']['Muerte']
                
                L_activs_d.append(x1)
                #print('Activos '+str(x1))
                
            if(i['attributes']['Estado'] == 'Confirmado'): 
                x2 = i['attributes']['Muerte']
                L_confrs_d.append(x2)
                #print('Confirmados '+str(x2))
                
            if(i['attributes']['Estado'] == 'Fallecido'): 
                x3 = i['attributes']['Muerte']
                L_fallds_d.append(x3)
                #print('Fallecidos '+str(x3))
            
            if(i['attributes']['Estado'] == 'Recuperado'): 
                x4 = i['attributes']['Muerte']
                L_recups_d.append(x4)
                #print('Recuperados '+str(x4))

    ax.plot(dias_Caso1, L_confrs_d, linestyle='-', marker='v', label='Casos Confirmados'  ,color='#2076FB')
    ax.plot(dias_Caso1, L_recups_d, linestyle='-', marker='<', label='Casos Recuperados'  ,color='#0DBB10')
    ax.plot(dias_Caso1, L_fallds_d, linestyle='-', marker='>', label='Casos Fallecidos'   ,color='#C725E1')
    ax.plot(dias_Caso1, L_activs_d, linestyle='-', marker='^', label='Casos Activos'      ,color='#EFEB0D')
    
    #Nombre
    ax.set_title('Resumen datos por día Covid-19 GT '+fechaH)
    ax.set(ylabel='Total de Casos',xlabel='Días a partir del caso 1')
    
    # Add a legend
    ax.legend()
    plt.legend(loc='upper left')
    
    #Show
    plt.show()
    
    #Save
    #Cambio de directorio
    #os.chdir('../imgs')
    #fig1.savefig("Casos_Diarios.png")
 '''