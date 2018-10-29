#import stuff
import random
from random import randint
import csv
import math

########################################################    Funktions
 
#NN wid zurückgesetzt
def randomizeNN(nameNN, index, distance):
    #bestimmtes File wird geöffnet
    with open(str(nameNN), 'w', newline='') as file:
        thewriter = csv.writer(file)
        #für jeden hidden layer wird 10*10 felder in der .csv datei hinzu gefügt
        for o in range(0, index*10):
            #10*10 Felder
            row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(0, 10):
                #jedes der Felder wird mit einem Zufallswert gefüllt
                row[i] = float(random.uniform(-float(distance), float(distance)))
            #speichern...
            thewriter.writerow(row)

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
    #führt möglicher weise zu problemen `\_O_/`
    #ausgabe
    return out

#Einlesen der Tabelle
def readTable(name):
    #funktioneiert!
    #nicht berühren!!!!!!!!!
    #einlesen
    r = csv.reader(open(name))
    #auflisten
    lines = list(r)
    #ausgabe
    return(lines)

#formartiert die .csv Datei für das Programm
def transformKurs(nameKurs):
    #einlesen der tabell
    kurs = readTable(nameKurs)
    #nur wenne es geändert werden muss
    if kurs[0][0] == 'Date':
        #print("start 'transformKurs'")
        newKurs = readTable(nameKurs)
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
        if lengthx>100:
            while lengthx>100:
                del newKurs[0]
                lengthx=lengthx-1
        #löscht die 2. Spalte weil die nicht mehr benötigt wird und nur verwirrt...
        for i in range(0, lengthx):
            del newKurs[i][1]
        # die Änderungen von NN werden als .csv gespeichert
        writer = csv.writer(open(nameKurs, 'w', newline=''))
        writer.writerows(newKurs)
        print("Kursdatei formatiert")
    else:
        print("Datei ist bereits formatiert")

#seperate the data für das Netztwerk als input
#da das NN nur die letzten 10 tage sehen soll
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
    #wiederholt für jeden weiteren hidden layer 
    #in 10'ner schritten weil ein hidden layer 10 spalten hat
    for i in range(10, length, 10):
        #layer2 wird geleert und berechnet
        layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        layer2 = layermalweights(layer1, weightsIn, i)
        #ergebniss wird an layer 1 weiter gegeben
        layer1 = layer2
        #so ergibt sich eine Scheife die es möglich mach unenlich lange NN zu bauen
    for o in range(0, len(layer1)):
        #output darf nur ein wert sein
        pass
        output = output + layer1[o]
    #output wird noch einmal bearbeitet
    output = sigmoid(output)
    #ausgabe
    return(output)

#berechnet den gesammtgewinn des NN über den vorhandenen Zeitraum
def getGesamt(kurseingabe, nneingabe):
    #Zeit
    time = 0
    gesamt = 0
    #gesammt berechnen
    for time in range(10, len(kurseingabe)):

        #sichtbare Daten für das NN als Eingabelayer werden sepperiert
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

        #gewinn wird dem gesammtgewinn zugerechnet
        gesamt = gesamt + gewinn
    return gesamt

#trifft voraussage für den nächsten Zeitabschnitt
def triffLiveVoraussage(nameKurs, nameNN):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = readTable(str(nameNN))

    #heißt für den neusten Wert
    time = 0

    #sichtbare Daten für das NN als Eingabelayer ermittelt
    daten = []
    daten = seperateData(kurs, len(kurs)-time)
    print("the NN sees:")
    #trinärumformung
    for i in range(0, len(daten)):
        var = sigmoid(float(daten[i]))
        if float(var)==1:
            print("+")
        if float(var)==-1:
            print("-")
        if float(var)==0:
            print("0")

    #Berechnung der Voraussage
    voraus = NNrechner(daten, NN)
    #trinärumformung
    if voraus>0:
        print("you should bet: +")
    if voraus<0:
        print("you should bet: -")
    if voraus==0:
        print("you should bet: 0")
    
#eigentlich nur die Funktion getGesamt mit Ausgabe
def useGetGesamt(nameKurs, nameNN):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = readTable(str(nameNN))

    #zum Beobachten
    gesamt = 0
    
    gesamt = getGesamt(kurs, NN)

    gesamt = (gesamt+100)/200*100

    print("gesamt: " + str(gesamt))
   