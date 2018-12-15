#import stuff
print("importing stuff...")
import base
import random
from random import randint
import math
import matplotlib.pyplot as plt


class NeuNet:
    
    def __init__(self, nameCSV, size=10):
        self.nameCSV = nameCSV
        self.NNlength = int(size)*10

    arrayNN = []
    NNweigth = 10
    distance = 2
    learningstats = []

    # sigmoud funktion
    # nicht wirklich (nur Verarbeitung)
    # wichtig bei Neuronale Netzten
    def sigmoid(self, x):
        out = (((1 / (1 + math.exp(-(x))))-0.5)*2)
        return out

    # Einlesen des NN aus einer CSV
    def readIn(self):
        self.arrayNN = base.readTable(self.nameCSV)
    
    # Exportieren des NN in eine CSV
    def saveOut(self):
        base.saveArray(self.arrayNN, self.nameCSV)

    # Setzt NN zurück
    def resetNN(self, ask=True):
        if ask==True:
            # ich glaube das geht besser
            if input('resetNN: ') == 'y':
                for i in range(0, self.NNlength):
                    for o in range(0, self.NNweigth):
                        self.arrayNN[i][o] = float(random.uniform(-self.distance, self.distance))
                print("done reset NN")
        else:
            for i in range(0, self.NNlength):
                for o in range(0, self.NNweigth):
                    self.arrayNN[i][o] = float(random.uniform(-self.distance, self.distance))


    # gibt einen Layer des NN aus
    def getOneLayer(self, index):
        # wird nur bei layermalweights gebraucht
        theLayer = []
        for i in range(index, index+self.NNweigth):
            theLayer.append(self.arrayNN[i])
        return theLayer

    # Matrixmultiplikation speziell für NN-Gewichtungen
    def layermalweights(self, layerIn, wightsIn):
        # das ist cool \/
        output = [0] * (self.NNweigth)
        for i in range(0, self.NNweigth):
            for o in range(0, self.NNweigth):
                output[i] = output[i] + (float(layerIn[o]) * float(wightsIn[o][i]))
        return(output)

    # Voraussage nach 10 Tagen (input)
    # Das Neuronale Netz
    def predict(self, daten, chart=None):
        output = 0
        chartdata = []
        chartcounter = 0
        # Verarbeitung des Inputs
        for i in range(0, len(daten)):
            if chart=="input":
                print(daten[i])
                chartcounter = chartcounter + daten[i]
                chartdata.append(chartcounter)
            daten[i] = self.sigmoid(float(daten[i]))
        if chart=="input":
            print()
        # Input gelangt in den ersten Layer des NN
        layer1 = [0] * (self.NNweigth)
        wigthsLayer = self.getOneLayer(0)
        layer1 = self.layermalweights(daten, wigthsLayer)
        # eine Layer wurde schon berechnet
        # arbeitet sich für jeden layer weiter
        # Einfach mal nachdenken und ausprobieren
        # Scheife die es möglich mach unenlich lange NN zu bauen
        for i in range(self.NNweigth, self.NNlength, self.NNweigth):
            # Layer2 wird mit Layer1 berechnet
            layer2 = [0] * (self.NNweigth)
            wigthsLayer = self.getOneLayer(i)
            layer2 = self.layermalweights(layer1, wigthsLayer)
            # Berechnung wird an Layer1 weiter gegeben
            for o in range(0, self.NNweigth):
                layer1[o] = self.sigmoid(layer2[o])
        for o in range(0, self.NNweigth):
            # Output ist nur ein Wert
            pass
            output = output + layer1[o]
        if chart=="input":
            chartcounter = chartcounter + output
            chartdata.append(chartcounter)
            plt.plot(chartdata)
            plt.ylabel('kurs')
            plt.show()
        #print(output)
        return(output)

    # gibt Testergebniss aus
    # wie gut es sich am Kurs geschlagen hat
    def getKnowledge(self, kurs):
        #Zeit
        time = 0
        gesamt = 0
        koennte = 0
        #gesammt berechnen
        for time in range(10, len(kurs)):
            # Daten für das NN als Eingabelayer sepperiert
            daten = []
            daten = base.seperateData(kurs, time)
            # Berechnung der Vorausagung
            voraussagung = self.predict(daten)
            realesGeschehen = float(kurs[time][0])
            # Berechnung des Gewinns
            gewinn = base.bewertung(realesGeschehen, voraussagung)
            # lokaler Gewinn wird dem Gesammtgewinn zugerechnet
            gesamt = gesamt + gewinn
            koennte = koennte+base.bewertung(realesGeschehen, realesGeschehen)
        gesamt = (gesamt/koennte)*100
        return gesamt

    # Trainiert Neuronales Netz
    def train(self, kurs, type=None):
        # Wissensindex vorher
        startKnowledge = self.getKnowledge(kurs)
        newKnowledge = 0
        if type == "Neuron":
            # Bestimmen eines Neuronens per zufall
            x = randint(0, len(self.arrayNN)-1)
            y = randint(0, len(self.arrayNN[x])-1)
            # Speichern
            save = self.arrayNN[x][y]
            # Änderung an dem Neuron vornehmen
            rand = random.uniform(-float(self.distance), float(self.distance))
            self.arrayNN[x][y] = float(self.arrayNN[x][y]) + rand
            # Wissensindex nachher
            newKnowledge = self.getKnowledge(kurs)
            if newKnowledge <= startKnowledge:
                # nimm den alten Wert wieder an
                self.arrayNN[x][y] = save

        if type == "Layer":
            # Python ist DUMMMMMMMMMMMMMM
            randomArray = []
            # Bestimmen eines Layers per zufall
            x=randint(0, len(self.arrayNN)-1)
            # Speichern
            save = self.arrayNN[x]
            # Änderung an dem Layer vornehmen
            rand = random.uniform(-float(self.distance), float(self.distance))
            for i in range(0, len(self.arrayNN[x])):
                randomArray.append(str(float(self.arrayNN[x][i])+rand))
            self.arrayNN[x] = randomArray
            # Wissensindex nachher
            newKnowledge = self.getKnowledge(kurs)
            if newKnowledge<=startKnowledge:
                # nimm die alten Werte wieder an
                self.arrayNN[x] = save
