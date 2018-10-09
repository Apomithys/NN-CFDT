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
def gues(neu, wette):
    return(neu * wette)

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
    print("pppppppppppppppppppppp: " + str(length))
    layer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    layer1 = layermalweights(layerIn, weightsIn, 0)
    for i in range(0, length):
        layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        layer2 = layermalweights(layer1, weightsIn, i)
        layer1 = layer2

    for o in range(0, len(layer1)):
        pass
        layerOut = layerOut + layer1[o]

    return(layerOut)

########################################################    Main part
def trainNNday(nameKurs, nameNN):
    print("start 'trainNNday'")

    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = readTable(str(nameNN))

    counter = int(input("how long: "))
    changes = 0
    maxchanges = 0
    
    #timelaps
    for count in range(0, counter):
        if counter == 777888999:
            count = 0


        #Zeit
        time = 0

        for time in range(10, len(kurs)):
            
            #sichtbare Daten für das NN als Eingabelayer
            daten = []
            daten = seperateData(kurs, time)
            
            #Berechnung der Vorausagung
            voraussagung = NNrechner(daten, NN)

            #Berechnung des gewinns
            gewinn = gues(float(kurs[time][0]), voraussagung)

            #Bestimmen des Neurons per zufall
            x = randint(0, len(NN)-1)
            y = randint(0, len(NN[x])-1)

            #sichern damit nichts kaputt geht
            save = 0
            save = NN[x][y]

            #erstmal davon ausgehen dass es schlecht ist
            better = False

            #ändere das ausgewählte Neuron
            NN[x][y] = -(float(NN[x][y]))

            #Berechnung der Vorausagung
            nvoraussagung = NNrechner(daten, NN)
            #Berechnung des gewinns
            ngewinn = gues(float(kurs[time][0]), nvoraussagung)

            #hatt es sich gebessert
            better = (gewinn < ngewinn)
            if better:
                changes = changes + 1

            #wenn es nicht besser geworden ist greife auf save zurück
            if better==False:
                NN[x][y] = save

        print(str(count) + " von " + str(counter) + " jahren trainiert and learnd " + str(changes) + " things")
        maxchanges = maxchanges + changes
        changes = 0

    #die Änderungen von NN werden als .csv gespeichert
    writer = csv.writer(open('NN.csv', 'w', newline=''))
    writer.writerows(NN)

    print(str(maxchanges) + " changes made")
