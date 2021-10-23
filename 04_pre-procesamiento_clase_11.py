#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:38:41 2021

@author: jorgek
"""
# 1 Outliers con Caja y bigote
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (10,10)
print('Outliers a partir de cajas - bigote')
# Outliers a partir de +/- 1,5 cajas
np.random.seed(153)
x_data = np.random.randn(100)
y_data = -x_data*.8 + np.random.randn(100)*0.5
df = pd.DataFrame()
df['vcnt'] = x_data
df['ecnt'] = y_data
left = 0.1
bottom = 0.1
top = 0.8
right = 0.8
main_ax = plt.axes([left,bottom,right-left,top-bottom])
# crear elemento axes (contornos de caja y bigote) arriba y a la derecha y ocultarlos.
top_ax = plt.axes([left,top,right - left,1-top])
plt.axis('off')
right_ax = plt.axes([right,bottom,1-right,top-bottom])
plt.axis('off')
main_ax.plot(df['vcnt'],  df['ecnt'], 'ko', alpha=0.5)
tcksx = main_ax.get_xticks()
tcksy = main_ax.get_yticks()
right_ax.boxplot(df['ecnt'], positions=[0], notch=False, widths=1.)
top_ax.boxplot(df['vcnt'], positions=[0], vert=False, notch=False, widths=1.)
#
main_ax.set_yticks(tcksy) # pos = tcksy
main_ax.set_xticks(tcksx) # pos = tcksx
main_ax.set_yticklabels([int(j) for j in tcksy])
main_ax.set_xticklabels([int(j) for j in tcksx])
main_ax.set_ylim([min(tcksy-1),max(tcksy)])
main_ax.set_xlim([min(tcksx-1),max(tcksx)])
main_ax.set_xlabel('Variable x')
main_ax.set_ylabel('Variable y')
# setear los límites
top_ax.set_xlim(main_ax.get_xlim())
top_ax.set_ylim(-1,1)
right_ax.set_ylim(main_ax.get_ylim())
right_ax.set_xlim(-1,1)
#%%
import pandas as pd
import numpy as np
#El Dataset 
df=pd.read_csv('iris.csv')
print('El dataset de Iris...')
#%%
# 2 Tipos de datos del dataset
input('Tipee algo para continuar...')
print(df.head)
tipos = df.columns.to_series().groupby(df.dtypes).groups
print(tipos)
# Listar Variables:
variables=df.columns.tolist()
print('Variables: ',variables)    
# Armando lista de variables cualitativas
ctext = tipos[np.dtype('object')]
print('Variables Cualitativas: ',ctext)
#Armado lista de variables numéricas
cnum = list(set(variables) - set(ctext))
print('Variables Numéricas: ',cnum)
#%%
# 3 Datos Vacíos:
# Controlando que no hayan valores faltantes
respuesta=input('En caso de NAN: ¿(R) Reemplazar / (E) Eliminar registro?')
if(respuesta=='R'):
    hayFaltantes=df.isnull().any().any()
    print('Hay datos vacios? ',hayFaltantes)
    # Si hay faltantes: competo a los numéricos con el promedio:
    for c in cnum:
        mean = df[c].mean()
        df[c] = df[c].fillna(mean)
    # Si hay faltantes cuantitativas completo:
    def completarVariableCualitativa(df,variable):
        var=[]
        for i in range(len(df)):
            if(pd.isna(df.iloc[i,variable])):
                dato='no_data'
            else:
                dato=df.iloc[i,variable]
            var.append(dato)
        return var
    ctext = tipos[np.dtype('object')]
    ctextnum=[]
    for i in range(len(ctext)):
        for j in range(len(variables)):
            if ctext[i]==variables[j]:
                ctextnum.append(j)
    for i in range(len(ctext)):
        completarVariableCualitativa(df,int(ctextnum[i]))
elif(respuesta=='E'):
    df = df.dropna(axis = 0, how ='any')
else:
    print('ERROR DESCONOCIDO')