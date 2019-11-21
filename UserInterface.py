import numpy as np
import matplotlib
import pandas as pd
import random as rd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
import ast

columnas = ['Modo','Sentimiento','Cantidad de Acordes','Grados','Experto']

def readKB():
    try:
        f = open("./ChordKB.csv")
        f.close()
    except:
        df = pd.DataFrame({'Modo':[],'Sentimiento':[],'Cantidad de Acordes':[],'Grados':[],'Experto':[]},
                        columns =['Modo','Sentimiento','Cantidad de Acordes','Grados','Experto'])
        df.to_csv("./ChordKB.csv",index = None, header = True)
        del df
    df = pd.read_csv("ChordKB.csv",sep = "/")
    return df

df = readKB()

def infer():
    df = readKB()
    global columnas
    ex = pd.DataFrame(df)
    for row in df.itertuples():
        #if row._3 < 4:
        for b in df.itertuples():
            if row.Modo == b.Modo and row.Sentimiento == b.Sentimiento:
                arr = ast.literal_eval(row.Grados)
                arr.extend(ast.literal_eval(b.Grados))
                cant = len(arr)
                m,s,e = row.Modo, row.Sentimiento, row.Experto
                ii = pd.DataFrame({'Modo':[m],'Sentimiento':[s],'Cantidad de Acordes':[cant],'Grados':[arr],'Experto':[e]},
                        columns =['Modo','Sentimiento','Cantidad de Acordes','Grados','Experto'])
                ex = ex.append(ii, ignore_index = True)
    return ex


def Search():
    Modo = str(modos.get())
    Sentimiento = str(sentimientos.get())
    Cant = int(cant.get())
    print(Modo, ' ', Sentimiento," ", Cant)
    df = infer()
    ex = pd.DataFrame()
    ex = df[df.Modo == Modo][df.Sentimiento == Sentimiento][df[columnas[2]] == Cant]
    if ex.empty:
        ex = df[df.Modo == Modo][df.Sentimiento == Sentimiento][df[columnas[2]] <= Cant]
        if ex.empty:
            ex = df[df.Modo == Modo][df.Sentimiento == Sentimiento]
            if ex.empty:
                ex = df[df.Modo == Modo]
                ex.append(df[df.Sentimiento == Sentimiento])
    print(ex)
    


def __init__(self):
    Modos = ['Jonico','Mixolidio']
    Sentimientos = ['Tristeza', 'Felicidad','Angustia','Exitante']
    Notas = ["C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","A#","Bb","B"]

    l_Modo = Label(self, text='Modo').place(x=10,y=10)
    cbx_Modo = ttk.Combobox(self, values = Modos, textvariable = modos).place(x=100,y=10)
    l_Sentimiento = Label(self, text = 'Sentimiento').place(x=10,y=35)
    cbx_Modo = ttk.Combobox(self, values=Sentimientos,textvariable = sentimientos).place(x=100,y=35)
    l_Cant = Label(self, text='Cantidad').place(x=10,y=60)
    spn_cant = Spinbox(self,from_ = 2,to = 10, increment = 1,textvariable = cant).place(x=100,y=60)
    btn_Search = Button(self, text = "Iniciar", command = Search).place(x=100, y=85)
    

ventana = Tk()
ventana.geometry('300x330')
ventana.title("UserInterface")


modos = StringVar()
sentimientos = StringVar()
cant = StringVar()


__init__(ventana)

ventana.mainloop()
