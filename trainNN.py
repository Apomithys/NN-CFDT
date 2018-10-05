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

#seperate the data für das Netztwerk als output
def seperateData(tabelle, t):
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    for p in range(t-10, t):
        data[counter] = tabelle[p][0]
        counter = counter + 1
    return(data)

#wetten, dass nach neu
def gues(alt, neu, wette):
    return((neu - alt) * wette)

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

counter = int(input("how long: "))
changes = 0

for i in range(0, counter):
    for time in range(10, len(kurs)-1):

        #sichtbare Daten für das NN als Eingabelayer
        daten = []
        daten = seperateData(kurs, time)
        #Berechnung der Vorausagung
        voraussagung = NNrechner(daten, NN)
        #Berechnung des gewinns
        gewinn = gues(float(kurs[time-1][0]), float(kurs[time][0]), voraussagung)

        #Bestimmen des Neurons per zufall
        x = randint(0, len(NN)-1)
        y = randint(0, len(NN[x])-1)

        #versichern damit nichts kaputt geht
        save = 0
        save = NN[x][y]

        #change
        NN[x][y] = random.uniform(-0.1, 0.1)

        #Berechnung der neuen Vorausagung
        nvoraussagung = NNrechner(daten, NN)
        #Berechnung des neuen Gewinns
        ngewinn = gues(float(kurs[time-1][0]), float(kurs[time][0]), nvoraussagung)

        #wenn es sich nich gebessert hat
        if gewinn > ngewinn:
            #zurücknehmen
            NN[x][y] = save
        else:
            changes = changes + 1

    #statusausgabe
    print(str(i) + " von " + str(counter) + " jahren trainiert!")
    
    #die Änderungen von NN werden als .csv gespeichert
    writer = csv.writer(open('NN.csv', 'w', newline=''))
    writer.writerows(NN)

print(str(changes) + " changes made")