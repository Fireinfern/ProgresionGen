import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk

columnas = ['Modo','Sentimiento','Cantidad de Acordes','Grados','Experto']

def readKB():
    try:
        f = open("./ChordKB.csv")
        f.close()
    except:
        df = pd.DataFrame({},
                        columns =['Modo','Sentimiento','Cantidad de Acordes','Grados','Experto'])
        df.to_csv("./ChordKB.csv",index = None, header = True, sep = '/')
        del df
    df = pd.read_csv("ChordKB.csv",sep = "/")
    return df




def __init__(self):
    Modos = ['Jonico','Mixolidio']
    Sentimientos = ['Tristeza', 'Felicidad','Angustia','Exitante']
    Notas = ["C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","A#","Bb","B"]

    l_Modo = Label(self, text='Modo').place(x=10,y=10)
    cbx_Modo = ttk.Combobox(self, values = Modos, textvariable = modos).place(x=100,y=10)
    l_Sentimiento = Label(self, text = 'Sentimiento').place(x=10,y=35)
    cbx_Modo = ttk.Combobox(self, values=Sentimientos,textvariable = sentimientos).place(x=100,y=35)
    l_Experto = Label(self,text='Nombre Experto').place(x=10,y=60)
    txt_Experto = ttk.Entry(self, textvariable = experto).place(x=100,y=60)
    l_Grado = Label(self, text ='Grado a Incertar').place(x=10,y = 85)
    txt_Grado = ttk.Entry(self, textvariable = grado).place(x=100,y = 85)
    btt_AgregarGrado = Button(self, text = "Agregar Grado a la progresion", command = agregarGrado).place(x=10,y=110)
    listbox_grados=Listbox(self,listvariable = Lista).place(x = 10,y=140)
    #btt_BorrarSelec = Button(self, text = "Borrar Grado",command=lambda lb=listbox_grados: lb.delete(ANCHOR)).place(x=150,y=140)
    btt_Guardar = Button(self, text = "Agregar",command = Agregar).place(x=150,y=170)
    btt_Limpiar = Button(self, text = "Limpiar", command = Limpiar).place(x=150,y=200)
    btt_dism = Button(self,text = "dim",command = Dim).place(x=230,y=85)

def Agregar():
    df = readKB()
    global columnas
    #t = np.array([[modos.get(),sentimientos.get(),len(ListaGrados),str(ListaGrados),experto.get()]])
    #df.append(pd.DataFrame([modos.get(),sentimientos.get(),len(ListaGrados),ListaGrados,experto.get()],columns = columnas), ignore_index = True)
    ##df1 = (pd.DataFrame(data=t,columns = columnas))
    #print(df1)
    df = df.append({columnas[0]:modos.get(),columnas[1]:sentimientos.get(),columnas[2]:len(ListaGrados)
                    ,columnas[3]:ListaGrados,columnas[4]:experto.get()}, ignore_index = True)
    df.to_csv('./ChordKB.csv',sep = '/',index = None, header =True)
   
def Dim():
    grado.set(grado.get() + "°")


def agregarGrado():
    if grado.get()!= '':
        ListaGrados.append(grado.get())
        Lista.set(ListaGrados)
        grado.set('')


ventana = Tk()
ventana.geometry('300x330')
ventana.title("ExpertInterface")


experto = StringVar()
modos = StringVar()
sentimientos = StringVar()
grado = StringVar()
ListaGrados = []
Lista = StringVar(value = ListaGrados)

def Limpiar():
    experto.set('')
    modos.set('')
    sentimientos.set('')
    global ListaGrados
    ListaGrados=[]
    Lista.set(value=ListaGrados)

__init__(ventana)

ventana.mainloop()
