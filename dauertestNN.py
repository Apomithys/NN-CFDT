#import stuff
import random
from random import randint
import csv
import funktions

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
    layerOut = 0
    length = int(len(weightsIn)/10) -1
    layer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer1 = layermalweights(layerIn, weightsIn, 0)
    #wegen hidden layer + in +out 
    for i in range(1, length+2):
        layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        layer2 = layermalweights(layer1, weightsIn, i)
        layer1 = layer2

    for o in range(0, len(layer1)):
        pass
        layerOut = layerOut + layer1[o]

    return(layerOut)


########################################################    Main part

def dauertestNN(nameKurs, nameNN):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = funktions.readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = funktions.readTable(str(nameNN))

    #Zeit
    time = 0

    #zum Beobachten
    gesamt = 0

    #timelaps
    for time in range(10, len(kurs)):
        #sichtbare Daten für das NN als Eingabelayer
        daten = []
        daten = funktions.seperateData(kurs, time)
        
        #Berechnung der Voraussage
        voraussage = NNrechner(daten, NN)
        #Berechnung des wettabfalls
        wettabfall = funktions.gues(float(kurs[time][0]), voraussage)
        #anrechnen an gesamtgewinn
        gesamt = gesamt + wettabfall

        #hier kann ausgegeben werden wass du willst (wettabfall/gesamt/voraussage)
        # print(time)
        # print(daten)
        # print(str(voraussage) + " * " + str(kurs[time][0]) + " = " + str(wettabfall))
    print("gesamt: " + str(gesamt))