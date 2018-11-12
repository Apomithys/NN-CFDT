import random
from random import randint
import time
import csv
import math

#noch nicht fertig
#downloadet .csv Deitei von yahoo!finance
def downloadKurs(name):
    pass
    #hier soll es mal eine Kursdatei automatisch herunterladen und als .csv Datei speichert

#NN wid zurückgesetzt
def randomizeNN(nameNN, index, distance):
    #bestimmtes File wird geöffnet
    print('ACHTUNG: NN wird zurückgesetzt')
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
    #führt möglicher weise zu problemen `\_O_/´
    #ausgabe
    
    # #echte sigmoid Funktion
    # out = 1 / (1 + math.exp(-x))

    return out

#Einlesen einer Tabelle (.csv)
def readTable(name):
    #funktioneiert!
    #nicht berühren!!!!!!!!!
    #einlesen
    r = csv.reader(open(name))
    #auflisten
    lines = list(r)
    #ausgabe
    return(lines)

#soll die Datei in der das NN gespeichert werden soll...
#daran hindern mehr als 100 zeilen zu bekommen...
#passiert manchmal `\_O_/´
def secureNN(NNarr):
    if len(NNarr)>100:
        print('Speicherfehler')
        print(len(NNarr))
        print(str(NNarr[len(NNarr)-1]))
        del NNarr[len(NNarr)-1][0]
        print('Speicherfehler behoben')
    return NNarr

#schneidet den Sichtbereich für das Netztwerk zu
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
    #ausgabe des outputlayers
    return(output)

#wetten, dass "nach" neu die "wette" eintritt
def gues(neu, wette):
    #binäre Variante
    out = 0
    zwi = neu * wette
    if zwi > 0:
        out = 1
    elif zwi < 0:
        out = -1
    elif zwi == 0:
        out = 0

    # #reale Variante
    # out = float(neu * wette)
    #ausgabe des gewinns
    return(out)

#speichert das NN in ein .csv File
def saveArray(array, csvname):
    writer = csv.writer(open(str(csvname), 'w', newline=''))
    writer.writerows(array)
