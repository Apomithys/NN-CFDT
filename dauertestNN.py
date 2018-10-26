#import stuff
import random
from random import randint
import csv
import funktions

########################################################    Main part
#eigentlich nur die Funktion getGesamt mit Ausgabe
def dauertestNN(nameKurs, nameNN):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = funktions.readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = funktions.readTable(str(nameNN))

    #zum Beobachten
    gesamt = 0
    
    gesamt = funktions.getGesamt(kurs, NN)

    print("gesamt: " + str(gesamt))
    