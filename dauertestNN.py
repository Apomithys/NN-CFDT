#import stuff
import random
from random import randint
import csv

########################################################    Funktions

#Einlesen der Tabelle
def readTable(name):
    r = csv.reader(open(name))
    lines = list(r)
    return(lines)

#wetten, dass nach neu
def gues(neu, wette):
    return(neu * wette)

#seperate the data für das Netztwerk als output
def seperateData(tabelle, t):
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    for p in range(t-10, t):
        data[counter] = tabelle[p][0]
        counter = counter + 1
    return(data)

#Einlesen der Tabelle "kurs.csv" als kurs
kurs = []
kurs = readTable("kurs.csv")

#Einlesender Tabelle "NN.csv" als NN
NN = []
NN = readTable("NN.csv")

########################################################    Network funktion

#matrixmultiplikation speziell für NN-Gewichtungen
def layermalweights(layerIn, NN, index):
    layerOut = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,9):
        for o in range(0,9):
            layerOut[i] = layerOut[i] + (float(layerIn[i]) * float(NN[o+index][i]))
    return(layerOut)

#Funktion mit einem Eingabelayer die einen Wert nach NN
def NNrechner(layerIn, weightsIn):
    #kann man das auch als for schleife machen ???
    layer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    layer1 = layermalweights(layerIn, weightsIn, 0)
    layer2 = layermalweights(layer1, weightsIn, 10)
    layer3 = layermalweights(layer2, weightsIn, 20)
    layer4 = layermalweights(layer3, weightsIn, 30)
    layer5 = layermalweights(layer4, weightsIn, 40)

    layerOut = 0
    for i in range(0, len(layer5)):
        layerOut = layerOut + layer5[i]
    return(layerOut)

########################################################    Main part

#Zeit
time = 0

#zum Beobachten
gesamt = 0

#timelaps
for time in range(len(kurs)-1, 10, -1):

    #sichtbare Daten für das NN als Eingabelayer
    daten = []
    daten = seperateData(kurs, time)
    print(daten)
    #Berechnung der Voraussage
    voraussage = NNrechner(daten, NN)
    #Berechnung des wettabfalls
    wettabfall = gues(float(kurs[time-11][0]), voraussage)
    #anrechnen an gesamtgewinn
    gesamt = gesamt + wettabfall

    #hier kann ausgegeben werden wass du willst (wettabfall/gesamt/voraussage)
    print(str(wettabfall) + " = " + str(voraussage) + " * " + str(kurs[time-10][0]))
    print("all: " + str(gesamt))
    print()