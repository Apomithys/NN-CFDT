#import stuff
import funktions
import random
from random import randint
import csv
import funktions

########################################################    Main part
def trainNNyear(nameKurs, nameNN, distance):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = funktions.readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = funktions.readTable(str(nameNN))

    counter = int(input("how long: "))
    changes = 0

    #Zeit
    time = 0
    gesamt = 0
    #gesammt berechnen
    for time in range(10, len(kurs)):

        #sichtbare Daten für das NN als Eingabelayer
        daten = []
        daten = funktions.seperateData(kurs, time)

        #Berechnung der Vorausagung
        voraussagung = funktions.NNrechner(daten, NN)
        #Berechnung des gewinns
        gewinn = funktions.gues(float(kurs[time][0]), voraussagung)

        gesamt = gesamt + gewinn
    print("gesamt am anfangg: "+ str(gesamt))

    #wiedeholung bis counter
    for count in range(0, counter):
        if counter == 777888999:
            count = 0

        print ('|', end="", flush=True)

        #Bestimmen des Neurons per zufall
        x = randint(0, len(NN)-1)
        y = randint(0, len(NN[x])-1)

        #sichern damit nichts kaputt geht
        save = 0
        save = NN[x][y]

        #better auf Fals setzen
        better = False

        #change
        #NN[x][y] = -float(NN[x][y])
        NN[x][y] = float(NN[x][y]) + random.uniform(-float(distance), float(distance))

        #Zeit
        time = 0
        ngesamt = 0
        #ngesammt berechnen
        for time in range(10, len(kurs)):

            #sichtbare Daten für das NN als Eingabelayer
            daten = []
            daten = funktions.seperateData(kurs, time)

            #Berechnung der Vorausagung
            nvoraussagung = funktions.NNrechner(daten, NN)
            #Berechnung des gewinns
            ngewinn = funktions.gues(float(kurs[time][0]), nvoraussagung)
            ngesamt = ngesamt + ngewinn

        #gucken ob gebessert hat
        better = (ngesamt > gesamt)
        # print(str(better) + " = " + str(ngesamt) + " > " + str(gesamt))
        
        #wenn es besser geworden ist
        if better == True:
            #addiere einen change dazu
            changes = changes+1
        #wenn es immernoch schlecht ist
        if better == False:
            #nimm das gesicherte
            NN[x][y] = save

        # print("it learned something: " + str(changes))
        
        #die Änderungen von NN werden als .csv gespeichert
        writer = csv.writer(open(str(nameNN), 'w', newline=''))
        writer.writerows(NN)
    print()
    print(str(changes) + " changes made")