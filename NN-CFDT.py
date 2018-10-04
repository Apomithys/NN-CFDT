#import stuff
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
    for i in range(0, len(tabelle)):
        for o in range(0, len(tabelle[i])):
            tabelle[i][o] = tabelle[i][o]

    #ausgebe
    #print(tabelle)
    return(tabelle)

#wetten, dass nach neu
def gues(alt, neu, wette):
    return((neu - alt) * wette)

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

NN = []
NN = readTable("NN.csv")

########################################################    Network funktion

def layermalweights(layerIn, NN, index):
    layerOut = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,9):
        for o in range(0,9):
            layerOut[i] = layerOut[i] + (float(layerIn[i]) * float(NN[o+index][i]))
    return(layerOut)

def NNrechner(layerIn, weightsIn):
    layer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    layer1 = layermalweights(layerIn, weightsIn, 0)
    layer2 = layermalweights(layer1, weightsIn, 10)
    layer3 = layermalweights(layer2, weightsIn, 20)
    layer4 = layermalweights(layer3, weightsIn, 30)

    layerOut = layer2[0]
    return(layerOut)

########################################################    Main part

money = 10

#Zeit
time = 0
for time in range(10, len(kurs)-100):
    #print("time: " + str(time))
    daten = []
    daten = seperateData(kurs, time)
    #Berechnung des wettabfalls
    wettabfall = gues(float(kurs[time-1][0]), float(kurs[time][0]), NNrechner(daten, NN))
    #Anrechnug ans Konto
    money = money + wettabfall
    print(money)
