
import random

import csv

########################################################    Funktions

#Einlesen der Tabelle
def readTable(name):

    #einlesen der Datei
    dateihandler = open(name)

    #inhalt ist langer String
    inhalt = dateihandler.read()

    #tabelle ist leere liste
    tabelle = []

    #in zeilen aufspalten
    zeilen = inhalt.split('\n')

    #in spalten aufspalten
    for i in range(len(zeilen)):
        spalten = zeilen[i].split(',')
        tabelle.append(spalten)

    #Strings umwandeln in Real
    for i in range(len(tabelle)-1):
        for o in range(len(tabelle[0])):
            tabelle[i][o] = float(tabelle[i][o])

    #ausgebe
    #print(tabelle)
    return(tabelle)

#Kurswette dass bit nach wette ausfällt
def gues(bit, wette):
    winn = wette*bit
    return(winn)

#seperate the data für das Netztwerk als output
def seperateData(tabelle, t):
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    for p in range(t-10, t):
        print(tabelle[p][1])
        data[counter] = tabelle[p][1]
        counter = counter + 1
    return(data)

#Einlesen der Tabelle "kurs.csv" als kurs
kurs = []
kurs = readTable("kurs.csv")

NN = []
NN = readTable("NN.csv")

########################################################    Network funktion

def NNrechner(layerIn, weightsIn):
    layer0 = layerIn
    weights0 = weightsIn
    layer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0,9):
        layer1[i] = layer1[i] + (layer0[i] * weights0[0][i])

    for i in range(0,9):
        layer2[i] = layer2[i] + (layer1[i] * weights0[1][i])
    layerOut = layer2[0]
    return(layerOut)

########################################################    Main part

money = 10

#Zeit
time = 0
for time in range(10, len(kurs)-1):
    daten = []
    daten = seperateData(kurs, time)
    print("time: " + str(time))
    #Berechnung des wettabfalls
    wettabfall = gues(float(kurs[time][1]), NNrechner(daten, NN))
    print(str(money) + " + " + str(wettabfall))
    #Anrechnug ans Konto
    money = money + wettabfall
    print("= " + str(money))
    print()
