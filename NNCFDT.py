#import stuff
print("importing stuff...")
import base
import random
from random import randint
import time
import csv
import math

########################################################    Funktions

#formartiert die .csv Datei mit den Kursdaten für das Programm
#schneidet es außerdem auf 100 Tage zu
def transformKurs(nameKurs):
    #einlesen der tabell
    kurs = base.readTable(nameKurs)
    #nur wenne es geändert werden muss
    if kurs[0][0] == 'Date':
        #print("start 'transformKurs'")
        newKurs = base.readTable(nameKurs)
        #größer der Tabelle 
        #spart Zeit auch für die Scheifen
        lengthx = len(newKurs)
        lengthy = len(newKurs[0])
        #tabelle mit 0'en erstellen
        #das muss besser gehen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #wiederhole für jede zeile und Spalte
        for i in range(0, lengthx):
            for o in range(0, lengthy):
                #setzte es auf null
                newKurs[i][o] = 0
        #print(newKurs)
        #steigung wrird berechnet und in 0 gepackt
        for i in range(1, lengthx-1):
            newKurs[i-1][0] = float(kurs[i+1][4]) - float(kurs[i][4])
        #packt die daten von 4 zu 1
        for i in range(1, lengthx):
            newKurs[i-1][1] = float(kurs[i][4])
        #löscht die letzten spalten mit nullen
        for i in range(0, lengthx):
            del newKurs[i][6]
            del newKurs[i][5]
            del newKurs[i][4]
            del newKurs[i][3]
            del newKurs[i][2]
        #print(newKurs)
        #lösche die letzten beiden zeilen
        #ertse war mal die 1. Zeile (hedder)
        del newKurs[lengthx-1]
        #zweite war die letzte die übrich bleibt beim berechnen der differenz der zeiten...
        del newKurs[lengthx-2]
        lengthx=lengthx-2
        #reduziert die Tabelle auf die letzten 100 Tage
        if lengthx>110:
            while lengthx>110:
                del newKurs[0]
                lengthx=lengthx-1
        #löscht die 2. Spalte weil die nicht mehr benötigt wird und nur verwirrt...
        for i in range(0, lengthx):
            del newKurs[i][1]
        base.saveArray(newKurs, nameKurs)
        print("Kursdatei formatiert")
    else:
        print("Datei ist bereits formatiert")

#das Neuronale Netz
#eingabe: name der Datei in der das NN gespeichert ist
#       : das was das NN als Input bekommt
#ausgabe: ein Wert (prdiction)
def NNrechner(layerIn, weightsIn):
    #sicherstellen dass es 100 zeilen hat
    weightsIn = base.secureNN(weightsIn)
    output = 0
    for i in range(0, len(layerIn)):
        layerIn[i] = base.sigmoid(float(layerIn[i]))
    #layer 1 wird geleert
    layer1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #vom input zum layer 1 gerechnet (1. hidden layer)
    layer1 = base.layermalweights(layerIn, weightsIn, 0)
    #wiederholt für jeden weiteren hidden layer 
    #in 10'ner schritten weil ein hidden layer 10 spalten hat
    for i in range(10, int(len(weightsIn)), 10):
        #layer2 wird geleert und berechnet
        layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        layer2 = base.layermalweights(layer1, weightsIn, i)
        #ergebniss wird an layer 1 weiter gegeben
        for o in range(len(layer2)):
            layer1[o] = base.sigmoid(layer2[o])
        #so ergibt sich eine Scheife die es möglich mach unenlich lange NN zu bauen
    layerlange=len(layer1)
    for o in range(0, layerlange):
        #output darf nur ein wert sein
        pass
        output = output + layer1[o]
    #output wird noch einmal bearbeitet
    output = base.sigmoid(output)
    #ausgabe
    return(output)

#berechnet den gesammtgewinn des NN über 100 Tage
def getGesamt(kurseingabe, nneingabe):
    #Zeit
    time = 0
    gesamt = 0
    #gesammt berechnen
    for time in range(10, len(kurseingabe)):

        #sichtbare Daten für das NN als Eingabelayer werden sepperiert
        daten = []
        daten = base.seperateData(kurseingabe, time)

        #Berechnung der Vorausagung
        voraussagung = NNrechner(daten, nneingabe)
        realesGeschehen = float(kurseingabe[time][0])

        #Berechnung des gewinns
        gewinn = base.gues(realesGeschehen, voraussagung)
        # print(str(voraussagung) + " Vorausgesagt")
        # print(str(realesGeschehen) + " Real")
        # print(str(gewinn) + " gewonnen")
        # print()

        #gewinn wird dem gesammtgewinn zugerechnet
        gesamt = gesamt + gewinn
    return gesamt

#trifft voraussage für den nächsten Zeitabschnitt
#nimmt sich die neusten Daten
def triffLiveVoraussage(kurs, NeuNet):

    #heißt für den neusten Wert
    time = 0

    #sichtbare Daten für das NN als Eingabelayer ermittelt
    daten = []
    daten = base.seperateData(kurs, len(kurs)-time)
    print("the NN sees:")
    #trinärumformung
    datenlänge=len(daten)
    for i in range(0, datenlänge):
        var = base.sigmoid(float(daten[i]))
        if float(var)==1:
            print("+")
        if float(var)==-1:
            print("-")
        if float(var)==0:
            print("0")

    #Berechnung der Voraussage
    voraus = NNrechner(daten, NeuNet)
    #trinärumformung
    if voraus>0:
        print("you should bet: +")
    if voraus<0:
        print("you should bet: -")
    if voraus==0:
        print("you should bet: 0")

#lernprozess
#dabei werden alle Synapsen von einem Neuronen verbessert
def trainNNlayer(kurs, NeuNet, distance):
    
    #wie lange soll es trainiert werden
    counter = 1+int(input("how long: "))
    
    gesamt = getGesamt(kurs, NeuNet)

    #wiedeholung bis counter
    for i in range(1, counter):
        print ('#', end="", flush=True)
        #Bestimmen der Neuronenreihe per zufall
        x = randint(0, len(NeuNet)-1)

        #sichern damit nichts kaputt geht
        save = [NeuNet[x][0], NeuNet[x][1], NeuNet[x][2], NeuNet[x][3], NeuNet[x][4], NeuNet[x][5], NeuNet[x][6], NeuNet[x][7], NeuNet[x][8], NeuNet[x][9]]
        
        rand = random.uniform(-float(distance), float(distance))
        #änderung an allen Neuronen
        for y in range(0, len(NeuNet[x])):
            # NN[x][y] = -float(NN[x][y])
            # NN[x][y] = float(NN[x][y]) + random.uniform(-float(distance), float(distance))
            NeuNet[x][y] = float(NeuNet[x][y]) + rand
        #ermitteln des neuen gewinns
        ngesamt = getGesamt(kurs, NeuNet)
                
        #wenn es besser geworden ist
        #print(str(ngesamt)+ " > " +str(gesamt))
        if ngesamt <= gesamt:
            pass
            #nimm das gesicherte
            for p in range(0, len(NeuNet[x])):
                NeuNet[x][p] = save[p]
        else:
            gesamt=ngesamt

            NeuNet = base.secureNN(NeuNet)

            print()
            print(str(i) + " / " + str(counter-1))
            print("gesammt: " + str(gesamt))

            print()
    return NeuNet

#lernprozess
#dabei wird nur eine Syapse verbessert
def trainNNneuron(kurs, NeuNet, distance):

    #wie lange soll es trainiert werden
    counter = 1+int(input("how long: "))

    gesamt = getGesamt(kurs, NeuNet)

    #wiedeholung bis counter
    for i in range(1, counter):
        print ('#', end="", flush=True)
        #Bestimmen der Neuronenreihe per zufall
        x = randint(0, len(NeuNet)-1)
        y = randint(0, len(NeuNet[x])-1)

        #sichern damit nichts kaputt geht
        save = 0
        save = NeuNet[x][y]

        #änderung an dem Neuron
        rand = random.uniform(-float(distance), float(distance))
        # NN[x][y] = -float(NN[x][y])
        # NN[x][y] = float(NN[x][y]) + random.uniform(-float(distance), float(distance))
        NeuNet[x][y] = float(NeuNet[x][y]) + rand
        #ermitteln des neuen gewinns
        ngesamt = getGesamt(kurs, NeuNet)
                
        #wenn es besser geworden ist
        #print(str(ngesamt)+ " > " +str(gesamt))
        if ngesamt <= gesamt:
            #nimm das gesicherte
            NeuNet[x][y] = save
        else:
            gesamt = ngesamt
            
            #die Änderungen von NN werden als .csv gespeichert
            NeuNet = base.secureNN(NeuNet)

            print()
            print(str(i) + " / " + str(counter-1))
            print("gesammt: " + str(gesamt))

            print()
    
    return NeuNet
