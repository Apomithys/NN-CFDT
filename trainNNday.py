#import stuff
import random
from random import randint
import csv
import funktions

########################################################    Main part
def trainNNday(nameKurs, nameNN, distance):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = funktions.readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = funktions.readTable(str(nameNN))

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
            daten = funktions.seperateData(kurs, time)
            
            #Berechnung der Vorausagung
            voraussagung = funktions.NNrechner(daten, NN)

            #Berechnung des gewinns
            gewinn = funktions.gues(float(kurs[time][0]), voraussagung)

            #Bestimmen des Neurons per zufall
            x = randint(0, len(NN)-1)
            y = randint(0, len(NN[x])-1)

            #sichern damit nichts kaputt geht
            save = 0
            save = NN[x][y]

            #erstmal davon ausgehen dass es schlecht ist
            better = False

            #ändere das ausgewählte Neuron
            #NN[x][y] = -float(NN[x][y])
            NN[x][y] = float(NN[x][y]) + random.uniform(-float(distance), float(distance))

            #Berechnung der Vorausagung
            nvoraussagung = funktions.NNrechner(daten, NN)
            #Berechnung des gewinns
            ngewinn = funktions.gues(float(kurs[time][0]), nvoraussagung)

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
    writer = csv.writer(open(nameNN, 'w', newline=''))
    writer.writerows(NN)

    print(str(maxchanges) + " changes made")
