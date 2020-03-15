#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1 de FSO-2019/20
Autors: Pedro Espadas
Data: 3/3/2020
Versio: 1.0
"""
# imports tipics/generics
import os

# imports pel GUI
from tkinter import *   # GUI
from tkinter import filedialog  # per a demanar fitxers
from tkinter import messagebox  # per a mostrar missatges a l’usuari

# imports específics d'aquesta practica
import sqlite3
import chardet
from urllib.parse import quote, unquote
import os.path
from subprocess import Popen, PIPE
import gzip
import io


def tracta_excepcio_sql(error, comandasql):
    exception_type = type(error).__name__
    print("\n" + exception_type, file=sys.stderr)
    print(error, file=sys.stderr)
    print(comandasql + "\n", file=sys.stderr)


# Crea la connexio i un cursor
# retorna: la connexio i el cursor
def crea_connexio(database_name):
    con = None
    cur = None  # Added to delete warning referenced before assignment
    try:
        con = sqlite3.connect(database_name)
        cur = con.cursor()
    except sqlite3.Error as err:
        tracta_excepcio_sql(err, "Inicialització DB")  # Connectar processos de sql
    return con, cur


def crea_taula(connection=None, cursor=None):
    # Create table
    sqlcmd = ""
    try:
        sqlcmd = '''CREATE TABLE LOGS (mes, dia, segons, minuts, hores, nomMaquina, nomProces, PID, missatge)'''
        cursor.execute(sqlcmd)
        connection.commit()
    except sqlite3.Error as error:
        tracta_excepcio_sql(error, sqlcmd)


def plenaTaula(fileHandler, compressed=False):
    if compressed:
        with gzip.open(logFileHandler.name, 'rb') as log_input:
            with io.TextIOWrapper(log_input, encoding='utf-8') as dec:
                content = dec.readlines()
    else:
        content = open(fileHandler.name, "rb")

    for i in content:
        if compressed:
            values = validateLine(i)

            linia = []
            for value in values:
                linia.append(str(value))
            print("line is: " + " ".join(linia))
        else:
            # Permet llegir fitxers binaris i en diferentes codificacions
            encoding = chardet.detect(i)
            i = i.decode(encoding['encoding'], 'ignore')
            values = validateLine(i)

            linia = []
            for value in values:
                linia.append(str(value))
            print("line is: " + " ".join(linia))

        if values:
            try:

                # Escape special characters
                for j in range(len(values)):
                    values[j] = quote(str(values[j]))

                # Insert a row of data
                sqlcmd = '''INSERT INTO LOGS VALUES(''' + "\"" + str(values[0]) + "\", \"" + str(values[1]) + "\", \"" + str(
                    values[2]) + "\", \"" + str(values[3]) + "\", \"" + str(values[4]) + "\", \"" + str(
                    values[5]) + "\", \"" + str(values[6]) + "\", \"" + str(values[7]) + "\", \"" + str(
                    values[8]) + "\"" + ")"
                cursor.execute(sqlcmd)

                # Save (commit) the changes
                connection.commit()
            except sqlite3.Error as error:
                tracta_excepcio_sql(error, str(sqlcmd))

        else:
            pass


def buscaMes():
    mesosPossibles = ["Gen", "Jan", "Feb", "Ene", "Mar", "May", "Mai", "Jun", "Jul", "Aug", "Ago", "Set", "Sep",
                      "Oct",
                      "Nov", "Des", "Dic", "Abr", "Apr"]
    try:
        entry = str(entrada.get())
        if len(entry) != 3:
            raise
        if entry not in mesosPossibles:
            raise
    except:
        print ("El format introduït del mes és incorrecte")
        return
    sqlcmd = '''SELECT * FROM LOGS WHERE mes = ''' + "\"" + entrada.get() + "\""
    cursor.execute(sqlcmd)
    connection.commit()
    lines = cursor.fetchall()
    listBoxEvents.delete(0, END)
    for line in lines:
        fields = []
        for field in line:
            field = unquote(str(field))
            fields.append(field)
        fields = " ".join(fields)

        listBoxEvents.insert(END, fields)

    n = len(lines)
    status.set("Elements filtrats: " + str(n))

    pass


def buscaData():
    data = entrada.get().split(" ")
    mes = str(data[0])
    data_dia = int(data[1])
    sqlcmd = "SELECT * FROM LOGS WHERE mes=" + "\"" + str(mes) + "\" AND dia=" + "\"" + str(data_dia) + "\""
    cursor.execute(sqlcmd)
    connection.commit()
    lines = cursor.fetchall()
    listBoxEvents.delete(0, END)
    for line in lines:
        fields = []
        for field in line:
            field = unquote(str(field))
            fields.append(field)
        fields = " ".join(fields)

        listBoxEvents.insert(END, fields)

    n = len(lines)
    status.set("Elements filtrats: " + str(n))


def buscaMaquina():
    sqlcmd = '''SELECT * FROM LOGS WHERE nomMaquina = ''' + "\"" + entrada.get() + "\""
    cursor.execute(sqlcmd)
    connection.commit()
    lines = cursor.fetchall()
    listBoxEvents.delete(0, END)
    for line in lines:
        fields = []
        for field in line:
            field = unquote(str(field))
            fields.append(field)
        fields = " ".join(fields)

        listBoxEvents.insert(END, fields)

    n = len(lines)
    status.set("Elements filtrats: " + str(n))


def buscaProces():
    sqlcmd = '''SELECT * FROM LOGS WHERE nomProces = ''' + "\"" + entrada.get() + "\""
    cursor.execute(sqlcmd)
    connection.commit()
    lines = cursor.fetchall()
    listBoxEvents.delete(0, END)
    for line in lines:
        fields = []
        for field in line:
            field = unquote(str(field))
            fields.append(field)
        fields = " ".join(fields)

        listBoxEvents.insert(END, fields)

    n = len(lines)
    status.set("Elements filtrats: " + str(n))


def buscaPID():
    sqlcmd = '''SELECT * FROM LOGS WHERE PID = ''' + "\"" + entrada.get() + "\""
    cursor.execute(sqlcmd)
    connection.commit()
    lines = cursor.fetchall()
    listBoxEvents.delete(0, END)
    for line in lines:
        fields = []
        for field in line:
            field = unquote(str(field))
            fields.append(field)
        fields = " ".join(fields)

        listBoxEvents.insert(END, fields)

    n = len(lines)
    status.set("Elements filtrats: " + str(n))


def buscaTots():
    sqlcmd = " SELECT * FROM LOGS "
    cursor.execute(sqlcmd)
    connection.commit()
    lines = cursor.fetchall()
    listBoxEvents.delete(0, END)
    for line in lines:
        fields = []
        for field in line:
            field = unquote(str(field))
            fields.append(field)
        fields = " ".join(fields)

        listBoxEvents.insert(END, fields)

    n = len(lines)
    status.set("Elements filtrats: " + str(n))


def acabar():
    cursor.close()
    tancaGUI()


# Mostra els events filtrats per la sortida.
# Si son tots hauria de coincidir amb l'entrada.
def exportaFiltrats():
    for line in listBoxEvents.get(0, END):
        print(str(line).strip())


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

    # Formato 1
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
        if mes not in mesosPossibles:
            print("Mes incorrecte", file=sys.stderr)
            raise
        if dia < 1 | dia > 31:
            print("Dia incorrecte", file=sys.stderr)
            raise
        if hores < 0 | hores > 23:
            print("Hora incorrecte", file=sys.stderr)
            raise
        if minuts < 0 | minuts > 59:
            print("Minuts incorrectes", file=sys.stderr)
            raise
        if segons < 0 | segons > 59:
            print("Segons incorrectes", file=sys.stderr)
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
        values.append(reescriuMissatge)
    except:
        pass
        # print ("Formato incorrecto")

    # Formato 2
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
            if mes not in mesosPossibles:
                print("Mes incorrecte", file=sys.stderr)
                raise
            if dia < 1 | dia > 31:
                print("Dia incorrecte", file=sys.stderr)
                raise

            if hores < 0 | hores > 23:
                print("Hora incorrecte", file=sys.stderr)
                raise
            if minuts < 0 | minuts > 59:
                print("Minuts incorrectes", file=sys.stderr)
                raise
            if segons < 0 | segons > 59:
                print("Segons incorrectes", file=sys.stderr)
                raise

            formato2 = True
            values.append(mes)
            values.append(dia)
            values.append(hores)
            values.append(minuts)
            values.append(segons)
            values.append(nomMaquina)
            values.append(nomProces)
            values.append("")
            values.append(reescriuMissatge)

        except:
            pass
    if not (formato1 | formato2):
        print("linea mal es: " + newline,file=sys.stderr)
        return values
    else:
        return values


# tkinter GUI
guiRoot = Tk()
guiRoot.title("Log-Migration")
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
messagebox.showinfo("Carregar fitxer de log", "Selecciona el fitxer de log a carregar")
logFileHandler = filedialog.askopenfile("r")
opcio = messagebox.askyesno("Nova DB", "Vols crear una DB nova?")
tiposFichero = ["data", "gz", "UTF-8", "NON-ISO", "ASCII"]
compressed = False
if opcio:
    # Comprovem tipus de fitxer
    proceso = Popen("file " + logFileHandler.name, shell=True, stdout=PIPE, stderr=PIPE)
    filetype = str(proceso.communicate()[0].decode("utf-8").split(" ")[1])
    if filetype.__eq__("gzip"):
        compressed = True
    else:
        compressed = False

    creation_time = os.path.getctime(logFileHandler.name)
    try:  # Remove silently
        os.remove(
            logFileHandler.name+"_" + str(creation_time).split(".")[1] + ".db")  # Ens assegurem que si escollim nova BD d'un fitxer existent comencem de nou
    except OSError:
        pass
    connection, cursor = crea_connexio(logFileHandler.name+"_" + str(creation_time).split(".")[1] + ".db")  # Crea una BD nova  # TODO es crearà un nou fitxer amb el nom depenent del dia (_ddmmaa). Per exemple: logs2db_311219.db.

    crea_taula(connection, cursor)  # La DB es nova, crea la unica taula que tenim
else:
    DBFileHandler = filedialog.askopenfile("r")  # Obrir fitxer de base de dades
    connection, cursor = crea_connexio(DBFileHandler.name)
plenaTaula(logFileHandler, compressed)  # Carrega els nous records
messagebox.showinfo("", "Fitxer de Log i BD carregats correctament")
buscaTots()  # Mostra per defecte tots els records

# al final del fitxer: bucle d'espera d'events asincrons de l'usuari
guiRoot.mainloop()
