#import stuff
import random
from random import randint
import csv
import math

########################################################    Funktions

#sigmoud funktion
def sigmoid(x):
    out=0
    if x>0:
        out=1
    if x<0:
        out-1
    return out

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
def gues(neu, wette):
    #return(neu * wette)
    winn=0
    if (neu*wette)>0:
        winn=1
    else:
        winn=-1
    return(winn)

#matrixmultiplikation speziell für NN-Gewichtungen
def layermalweights(layerIn, NN, index):
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,9):
        for o in range(0,9):
            output[i] = output[i] + (float(layerIn[i]) * float(NN[o+index][i]))
        output[i]=sigmoid(output[i])
    return(output)

#Funktion mit einem Eingabelayer die einen Wert nach NN
def NNrechner(layerIn, weightsIn):
    output = 0
    #anzahl der hidden layer
    #außerdem wird das Programm schneller
    length = int(len(weightsIn))
    #layer 1 wird geleert
    layer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #vom input zum layer 1 gerechnet (1. hidden layer)
    layer1 = layermalweights(layerIn, weightsIn, 0)
    print(layerIn)
    #wiederholt für jeden hidden layer 
    for i in range(10, length, 10):
        #layer2 wird geleert und berechnet
        layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        layer2 = layermalweights(layer1, weightsIn, i)
        #ergebniss wird an layer 1 weiter gegeben
        layer1 = layer2
    print(layer1)
    for o in range(0, len(layer1)):
        pass
        output = output + layer1[o]
    
    output = sigmoid(output)
    print(output)
    return(output)

def getGesamt(kurseingabe, nneingabe):
    #Zeit
    time = 0
    gesamt = 0
    #gesammt berechnen
    for time in range(10, len(kurseingabe)):

        #sichtbare Daten für das NN als Eingabelayer
        daten = []
        daten = seperateData(kurseingabe, time)

        #Berechnung der Vorausagung
        voraussagung = NNrechner(daten, nneingabe)
        realesGeschehen = float(kurseingabe[time][0])
        #Berechnung des gewinns
        gewinn = gues(realesGeschehen, voraussagung)
        # print(str(voraussagung) + " Vorausgesagt")
        # print(str(realesGeschehen) + " Real")
        # print(str(gewinn) + " gewonnen")
        # print()
        gesamt = gesamt + gewinn
    return gesamt
