#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#import sys
#import errno
#import time #Para poder usar el time.sleep(5)

yearInput = raw_input("Anio: ")
baseFolderInput = raw_input("Carpeta: ")
comboInput = raw_input("Combo: ")


folders = {
    yearInput+"/"+baseFolderInput+"/Seleccion/DVD",
    yearInput+"/"+baseFolderInput+"/Seleccion/TapaDVD",
    yearInput+"/"+baseFolderInput+"/Otros",
}

combos = {
    '1': {
        yearInput+"/"+baseFolderInput+"/20x30",
        yearInput+"/"+baseFolderInput+"/5 copias",
    },
    '2': {
        yearInput+"/"+baseFolderInput+"/20x30",
        yearInput+"/"+baseFolderInput+"/30x45",
        yearInput+"/"+baseFolderInput+"/7 copias",
    }
}

print "-------------------------------"
print "Creando la carpeta principal:"
print "-------------------------------"
print baseFolderInput
print ""
print "-------------------------------"
print "Creando carpetas secundarias:"
print "-------------------------------"
for folder in folders:
    if not os.path.exists(folder):
        print "Creando: " + folder + "..."
        os.makedirs(folder)
    else:
        print "La carpeta " + folder + " ya existe"
print ""
print "-------------------------------"
print "Creando carpetas para combos:"
print "-------------------------------"
for combo in combos[comboInput]:
    if not os.path.exists(combo):
        print "Creando: " + combo + "..."
        os.makedirs(combo)
    else:
        print "La carpeta " + combo + " ya existe"
print ""
print "-------------------------------"
print "FIN"
print "-------------------------------"
print "Listo! ya podes seguir adelante!\n\n"
print ""
raw_input("Press Enter to exit...")