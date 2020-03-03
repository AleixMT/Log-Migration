#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Practica 1 de FSO-2019/20
# Autors:
# Data:
# Versio:

# imports tipics/generics
import os   # os.path, os.stat, os.remove ...
from sys import stderr
from stat import filemode

# imports pel GUI
from tkinter import *   # GUI
from tkinter import filedialog	# per a demanar fitxers
from tkinter import messagebox	# per a mostrar missatges a l’usuari
# https://docs.python.org/3.9/library/tkinter.messagebox.html

# imports específics d'aquesta practica
import sqlite3

# imports auxilliars/secondaris
from time import strftime   # nom de la BD variable
import urllib.parse         # guardar events a la DB amb cars especials
import gzip                 # per si el log esta comprimit

#### BD SQLITE
# https://docs.python.org/3/library/sqlite3.html

def tracta_exepcio_sql(error, sql):
    exception_type = type(error).__name__
    print("\n",exception_type, file=sys.stderr)
    print(error, file=sys.stderr)
    print(sql,"\n", file=sys.stderr)

def crea_connexio(database):
    """ crea la connexio i un cursor
        retorna: la connexio i el cursor
        """
    con = None;
    try:
        con = sqlite3.connect(database)
        cur = con.cursor()
    except sqlite3.Error as error:
        tracta_exepcio_sql(err, sqlcmd)
    return con, cur

def crea_taula(cur, taula_sql):
    try:
        cur.execute(taula_sql)
    except sqlite3.Error as error:
        tracta_exepcio_sql(error, taula_sql)

# definicio de la taula amb els camps dels logs
sql_crea_taula = """CREATE TABLE events (
# >>>>>>>>>> CODI ALUMNES <<<<<<<<<<
                        .....
                        );"""

#### IMPORTAR FITXER DE LOG a BD
# >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

#### QUERIES SQL a la BD
# >>>>>>>>>> CODI ALUMNES <<<<<<<<<<
def buscaMes():
    n=66
    status.set("Elements filtrats: "+str(n))
    pass
def buscaData():
    pass
def buscaMaquina():
    pass
def buscaProces():
    pass
def buscaPID():
    pass
def buscaTots():
    pass
def acabar():
    tancaGUI()
    pass
def exportaFiltrats():
    """ Mostra els events filtrats per la sortida.
        Si son tots hauria de coincidir amb la entrada.
        """
    pass

#### tkinter GUI
# No cal mes informacio, pero si teniu curiositat,
# sense entar en molts detalls tcl/tk:
# https://likegeeks.com/es/ejemplos-de-la-gui-de-python/

guiroot= Tk()
guiroot.title("Filtar entrades de LOG a la BD")
guiroot.minsize(600,400)
cerca= StringVar()  # variable usada en els QUERIES

def tancaGUI():
    guiroot.quit()

# layout del GUI: 4 marcs apilats
frameCerca= Frame(guiroot)
frameBotons= Frame(guiroot)
frameEvents= Frame(guiroot)
frameStatus= Frame(guiroot)

# Frame CERCA
etiq= Label (frameCerca, text="Cerca")
etiq.pack(side=LEFT)
entrada= Entry(frameCerca, textvariable=cerca, width=80, bd=5)
entrada.pack(side=LEFT)
frameCerca.pack(side=TOP, expand=FALSE,fill=X,padx=2)

# Frame Botons
# Les funcions/commands les han d'implementar els alumnes
Button (frameBotons, text='Tots', command=buscaTots).pack(anchor=W,side=LEFT)
Button (frameBotons, text='Mes', command=buscaMes).pack(anchor=W,side=LEFT)
Button (frameBotons, text='Data', command=buscaData).pack(anchor=W,side=LEFT)
Button (frameBotons, text='Maq', command=buscaMaquina).pack(anchor=W,side=LEFT)
Button (frameBotons, text='Proc', command=buscaProces).pack(anchor=W,side=LEFT)
Button (frameBotons, text='PID', command=buscaPID).pack(anchor=W,side=LEFT)
Button (frameBotons, text='Sortir',command=acabar).pack(anchor=E, side=RIGHT)
Button (frameBotons, text='Exporta', command=exportaFiltrats).pack(anchor='e',side=RIGHT)
frameBotons.pack(expand=FALSE,fill=X,padx=40)

# Frame Events
Label (frameEvents,text='Events Filtrats:').pack(anchor=W,side=TOP)
scrollist = Scrollbar(frameEvents,orient=VERTICAL)
# llista on es quarden els events filtrats
lbox_events = Listbox(frameEvents,yscrollcommand=scrollist.set,selectmode=SINGLE,exportselection=False)
scrollist.config(command=lbox_events.yview)
scrollist.pack(side=RIGHT,fill=Y)
lbox_events.pack(side=LEFT,expand=True,fill=BOTH)
frameEvents.pack(side=TOP, expand=True,fill=BOTH,padx=2)

# Frame estat
status= StringVar()
status.set("Elements filtrats: 0")
etqStatus= Label (frameStatus, textvariable= status)
etqStatus.pack(side=RIGHT, anchor=E)
frameStatus.pack(side=RIGHT,expand=False,padx=2)

#### MAIN

nova= messagebox.askyesno("Nova DB o vella", "Vols crear una DB nova ?")

# >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

# al final del fitxer: bucle d'espera d'events asincrons de l'usuari
guiroot.mainloop()
