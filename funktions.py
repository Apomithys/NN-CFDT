#import stuff
import random
from random import randint
import csv
import math

########################################################    Funktions

#sigmoud funktion
#nicht wirklich (nur vrearbeitung des Inputs)
def sigmoid(x):
    #0 means unentschlossen
    out=0
    if x>0:
        #1 heoßt steigen
        out=1
    if x<0:
        #-1 heißt fallend
        out=-1
    #es kann aber auch 0 raus kommen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #führt möglicher weise zu problemen
    #ausgabe
    return out

#Einlesen der Tabelle
def readTable(name):
    #funktioneiert!
    #einlesen
    r = csv.reader(open(name))
    #auflisten
    lines = list(r)
    #ausgabe
    return(lines)

#seperate the data für das Netztwerk als input
def seperateData(tabelle, t):
    #tabelle ist die kustabelle
    #t ist die Zeit (0 heißt Live-Voraussage)
    #letzten 10 Tage
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #
    counter = 0
    #von tag 10 zu tag 0
    for p in range(t-10, t):
        #counter muss immer zwischen 0 und 10 sein
        #p allerdings ziemlich hoch
        #also gibt es 2 zählervariablen
        data[counter] = tabelle[p][0]
        #counter ist 2. zählervariable
        counter += 1
    #ausgabe der daten
    return(data)

#wetten, dass "nach" neu die "wette" eintritt
def gues(neu, wette):
    #return(neu * wette)
    #hier kann man noch einen one-liner draus machen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #kein gewinn
    winn = 0
    #"vor" ist es eine wahre Aussage kommt positiv else nevativ
    vor = (neu*wette)
    #verarbeitung zu -1; 0 oder +1
    winn = sigmoid(vor)
    #ausgabe des gewinns
    return(winn)

#matrixmultiplikation speziell für NN-Gewichtungen
def layermalweights(layerIn, NN, index):
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #wenn man es verstehen will...
    #schreibtischtest machen!!!!!!!!!
    #outputlayer ist der outputlayer
    #inputlayer ist inputlayer
    #NN ist tabelle mit der Breite 10 und einer Länge von hiddenlayer*10
    for i in range(0,9):
        for o in range(0,9):
            output[i] = output[i] + (float(layerIn[o]) * float(NN[o+index][i]))
        #jedes neuron des outputlayers erfährt noch einmal eine Verarbeitung
        output[i]=sigmoid(output[i])
    #ausgabe des outputlayers
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
    #wiederholt für jeden hidden layer 
    for i in range(10, length, 10):
        #layer2 wird geleert und berechnet
        layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        layer2 = layermalweights(layer1, weightsIn, i)
        #ergebniss wird an layer 1 weiter gegeben
        layer1 = layer2
    for o in range(0, len(layer1)):
        pass
        output = output + layer1[o]
    
    output = sigmoid(output)
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
