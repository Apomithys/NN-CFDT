#import stuff
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
    for i in range(0, length):
        layer2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        layer2 = layermalweights(layer1, weightsIn, i)
        layer1 = layer2

    for o in range(0, len(layer1)):
        pass
        layerOut = layerOut + layer1[o]

    return(layerOut)

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
    einsatzvor = NNrechner(daten, NN)
    print("you should bet: " + str(einsatzvor))