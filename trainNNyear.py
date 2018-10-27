#import stuff
import funktions
import random
from random import randint
import csv

########################################################    Main part
def trainNNyear(nameKurs, nameNN, distance):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = funktions.readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = funktions.readTable(str(nameNN))

    #wie lange soll es trainiert werden
    counter = int(input("how long: "))
    changes = 0

    #wiedeholung bis counter
    for i in range(0, counter):
        print ('#', end="", flush=True)
        gesamt = funktions.getGesamt(kurs, NN)
        #Bestimmen des Neurons per zufall
        x = randint(0, len(NN)-1)
        y = randint(0, len(NN[x])-1)

        #sichern damit nichts kaputt geht
        save = 0
        save = NN[x][y]

        #änderung an einem Neuron
        rand = random.uniform(-float(distance), float(distance))

        # NN[x][y] = -float(NN[x][y])
        # NN[x][y] = float(NN[x][y]) + random.uniform(-float(distance), float(distance))
        NN[x][y] = float(NN[x][y]) + rand

        #ermitteln des neuen gewinns
        ngesamt = funktions.getGesamt(kurs, NN)
                
        #wenn es besser geworden ist
        #print(str(ngesamt)+ " > " +str(gesamt))
        if (ngesamt > gesamt) == True:
            #addiere einen change dazu
            changes = changes+1
        #wenn es immernoch schlecht ist
        else:
            pass
            #nimm das gesicherte
            NN[x][y] = save
        
    #die Änderungen von NN werden als .csv gespeichert
    writer = csv.writer(open(str(nameNN), 'w', newline=''))
    writer.writerows(NN)
    print()
    print(str(changes) + " changes made")