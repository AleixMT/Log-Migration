#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1 de FSO-2019/20
Autors: Pedro Espadas
Data: 3/3/2020
Versio: 1.0
"""
# imports tipics/generics
# import sys
# import os   # os.path, os.stat, os.remove ...
# from sys import stderr
# from stat import filemode

# imports pel GUI
from tkinter import *   # GUI
from tkinter import filedialog	# per a demanar fitxers
from tkinter import messagebox  # per a mostrar missatges a l’usuari
# https://docs.python.org/3.9/library/tkinter.messagebox.html

# imports específics d'aquesta practica
import sqlite3


# imports auxiliars/secondaris
# from time import strftime   # nom de la BD variable
# import urllib.parse         # guardar events a la DB amb cars especials
# import gzip                 # per si el log esta comprimit


# BD SQLITE
def tracta_excepcio_sql(error, sql):
    exception_type = type(error).__name__
    print("\n", exception_type, file=sys.stderr)
    print(error, file=sys.stderr)
    print(sql, "\n", file=sys.stderr)


# Crea la connexio i un cursor
# retorna: la connexio i el cursor
def crea_connexio(nomBD):
    con = None
    cur = None  # Added to delete warning referenced before assignment
    sqlcmd = None  # Added to delete warning referenced before assignment
    try:
        sqlcmd = None  # Connectar proces de sql
        con = sqlite3.connect(nomBD)
        cur = con.cursor()
    except sqlite3.Error as err:
        tracta_excepcio_sql(err, sqlcmd)  # Connectar processos de sql
    return con, cur


def crea_taula(fileHandler, connection=None, cursor=None):
    # poden tenir diverses codificacions(ascii, utf - 8, etc)
    # poden contenir parts binàries
    # poden estar comprimits amb gzip(ex: syslog.2.gz)


    # Create table
    try:
        sqlcmd = '''CREATE TABLE LOGS
                             (mes, dia, segons, minuts, hores, nomMaquina, nomProces, PID, missatge)'''

        cursor.execute(sqlcmd)
    except sqlite3.Error as error:

        tracta_excepcio_sql(error, sqlcmd)


    
    for line in fileHandler.readlines():
        values = validateLine(line)
        if values :
            try:
                # Insert a row of data
                cursor.execute("INSERT INTO LOGS VALUES (values[0],values[1],values[2],values[3],values[4],values[5],values[6])")
                # Save (commit) the changes
                cursor.commit()
            except sqlite3.Error as error:
                tracta_excepcio_sql(error, sqlcmd)



            print ("Validat Correctament")
            print (values)
        else:
            print ("Validat Incorrectament")
            pass

    cursor.close()





    # Definicio de la taula amb els camps dels logs


    sql_crea_taula = """CREATE TABLE events (
    # >>>>>>>>>> CODI ALUMNES <<<<<<<<<<
                       .....
                        );"""


    # IMPORTAR FITXER DE LOG a BD
    # >>>>>>>>>> CODI ALUMNES <<<<<<<<<<



def buscaMes():
    # QUERIES SQL a la BD >>>>>>>>>> CODI ALUMNES <<<<<<<<<<
    n = 66
    status.set("Elements filtrats: " + str(n))
    pass


def buscaData():
    # QUERIES SQL a la BD >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

    pass


def buscaMaquina():
    # QUERIES SQL a la BD >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

    pass


def buscaProces():
    # QUERIES SQL a la BD >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

    pass


def buscaPID():
    # QUERIES SQL a la BD >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

    pass


def buscaTots():
    # QUERIES SQL a la BD >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

    pass


def acabar():
    tancaGUI()
    pass


# Mostra els events filtrats per la sortida.
# Si son tots hauria de coincidir amb la entrada.
def exportaFiltrats():
    pass


def tancaGUI():
    guiRoot.quit()

def validateLine(line):

    mesosPossibles = ["Gen", "Jan", "Feb", "Ene", "Mar", "May", "Mai", "Jun", "Jul", "Aug", "Ago", "Set", "Sep", "Oct",
                      "Nov", "Des", "Dic", "Abr", "Apr"]
    values = []
    # Eliminar espais repetits
    newline = ""
    first = True
    for i in range(len(line)):
        actualchar = line[len(line) - 1]
        if actualchar.__eq__(" "):
            if first:
                newline = actualchar + newline
                first = False
            else:
                pass
        else:
            newline = actualchar + newline
            first = True
        if len(line) - 1 > 0:
            line = line[0:len(line) - 1]

    #Formato 1
    formato1 = False
    try:
        camps = newline.split(" ")
        mes = camps[0]
        dia = int(camps[1])
        temps = camps[2]
        tempsCamps = temps.split(":")
        hores = int(tempsCamps[0])
        minuts = int(tempsCamps[1])
        segons = int(tempsCamps[2])
        nomMaquina = camps[3]
        nomProcesPID = camps[4]
        nomProcesPID = nomProcesPID.split("[")
        nomDimoni = nomProcesPID[0]
        PID = int(nomProcesPID[1].split("]")[0])




        missatge = camps[5:]
        reescriuMissatge = " ".join(missatge)
        print (missatge)
        print (reescriuMissatge)
        if mes not in mesosPossibles:
            print("Mes incorrecte")
            raise
        if dia < 1 | dia > 31:
            print("Dia incorrecte")
            raise

        if hores < 0 | hores > 23:
            print("Hora incorrecte")
            raise
        if minuts < 0 | minuts > 59:
            print("Minuts incorrectes")
            raise
        if segons < 0 | segons > 59:
            print("Segons incorrectes")
            raise

        formato1 = True
        values.append(mes)
        values.append(dia)
        values.append(hores)
        values.append(minuts)
        values.append(segons)
        values.append(nomMaquina)
        values.append(nomDimoni)
        values.append(PID)
        values.append (missatge)


    except:

        print ("Formato incorrecto")

    #Formato 2
    formato2 = False
    if not formato1:
        try:
            camps = newline.split(" ")
            mes = camps[0]
            dia = int(camps[1])
            temps = camps[2]
            tempsCamps = temps.split(":")
            hores = int(tempsCamps[0])
            minuts = int(tempsCamps[1])
            segons = int(tempsCamps[2])
            nomMaquina = camps[3]
            nomProces= camps[4]
            missatge = camps[5:]
            reescriuMissatge = " ".join(missatge)
            print(missatge)
            print(reescriuMissatge)
            if mes not in mesosPossibles:
                print("Mes incorrecte")
                raise
            if dia < 1 | dia > 31:
                print("Dia incorrecte")
                raise

            if hores < 0 | hores > 23:
                print("Hora incorrecte")
                raise
            if minuts < 0 | minuts > 59:
                print("Minuts incorrectes")
                raise
            if segons < 0 | segons > 59:
                print("Segons incorrectes")
                raise

            formato2 = True
            values.append(mes)
            values.append(dia)
            values.append(hores)
            values.append(minuts)
            values.append(segons)
            values.append(nomMaquina)
            values.append(nomProces)
            values.append ("")
            values.append(missatge)

        except:

            print("Formato incorrecto")

    if not (formato1 | formato2):
        print("esto es lalinea: " + newline)
        print(newline, file=sys.stderr)
        return values
    else:
        return values







# tkinter GUI
guiRoot = Tk()
guiRoot.title("Filtrar entrades de LOG a la BD")
guiRoot.minsize(600, 400)
cerca = StringVar()  # variable usada en els QUERIES

# layout del GUI: 4 marcs apilats
frameCerca = Frame(guiRoot)
frameBotons = Frame(guiRoot)
frameEvents = Frame(guiRoot)
frameStatus = Frame(guiRoot)

# Frame CERCA
etiqueta = Label(frameCerca, text="Cerca")
etiqueta.pack(side=LEFT)
entrada = Entry(frameCerca, textvariable=cerca, width=80, bd=5)
entrada.pack(side=LEFT)
frameCerca.pack(side=TOP, expand=FALSE, fill=X, padx=2)

# Frame Botons
# Les funcions/commands les han d'implementar els alumnes
Button(frameBotons, text='Tots', command=buscaTots).pack(anchor=W, side=LEFT)
Button(frameBotons, text='Mes', command=buscaMes).pack(anchor=W, side=LEFT)
Button(frameBotons, text='Data', command=buscaData).pack(anchor=W, side=LEFT)
Button(frameBotons, text='Maq', command=buscaMaquina).pack(anchor=W, side=LEFT)
Button(frameBotons, text='Proc', command=buscaProces).pack(anchor=W, side=LEFT)
Button(frameBotons, text='PID', command=buscaPID).pack(anchor=W, side=LEFT)
Button(frameBotons, text='Sortir', command=acabar).pack(anchor=E, side=RIGHT)
Button(frameBotons, text='Exporta', command=exportaFiltrats).pack(anchor='e', side=RIGHT)
frameBotons.pack(expand=FALSE, fill=X, padx=40)

# Frame Events
Label(frameEvents, text='Events Filtrats:').pack(anchor=W, side=TOP)
scrollList = Scrollbar(frameEvents, orient=VERTICAL)
# llista on es quarden els events filtrats
listBoxEvents = Listbox(frameEvents, yscrollcommand=scrollList.set, selectmode=SINGLE, exportselection=False)
scrollList.config(command=listBoxEvents.yview)
scrollList.pack(side=RIGHT, fill=Y)
listBoxEvents.pack(side=LEFT, expand=True, fill=BOTH)
frameEvents.pack(side=TOP, expand=True, fill=BOTH, padx=2)

# Frame estat
status = StringVar()
status.set("Elements filtrats: 0")
etqStatus = Label(frameStatus, textvariable=status)
etqStatus.pack(side=RIGHT, anchor=E)
frameStatus.pack(side=RIGHT, expand=False, padx=2)

# MAIN

nova = messagebox.askyesno("Nova DB o vella", "Vols crear una DB nova ?")
logFileHandler = filedialog.askopenfile("r")

if nova:
    connection, cursor = crea_connexio(logFileHandler.name+".db") #Crea una connexio

    pass
else:
    DBFileHandler = filedialog.askopenfile("r") #"Obrir fitxer de base de dades"
    connection, cursor = crea_connexio(DBFileHandler.name)

    pass
#BD READY
crea_taula(logFileHandler, connection, cursor)








# >>>>>>>>>> CODI ALUMNES <<<<<<<<<<

# al final del fitxer: bucle d'espera d'events asincrons de l'usuari
guiRoot.mainloop()
