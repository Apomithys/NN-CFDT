#import stuff
import funktions

########################################################    Main part

def triffVoraussage(nameKurs, nameNN):
    #Einlesen der Tabelle "kurs.csv" als kurs
    kurs = []
    kurs = funktions.readTable(str(nameKurs))

    #Einlesender Tabelle "NN.csv" als NN
    NN = []
    NN = funktions.readTable(str(nameNN))

    time = int(input("time(type 0 to see latest): "))

    #sichtbare Daten für das NN als Eingabelayer
    daten = []
    daten = funktions.seperateData(kurs, len(kurs)-time)
    print("the NN sees:")
    for i in range(0, len(daten)):
        print(str(daten[i]))

    #Berechnung des wettabfalls
    einsatzvor = funktions.NNrechner(daten, NN)
    print("you should bet: " + str(einsatzvor))