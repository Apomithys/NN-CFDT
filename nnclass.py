#import stuff
print("importing stuff...")
import base
import random
from random import randint
import math


class NeuNet:
    
    arrayNN = []
    NNlength = 100
    NNweigth = 10
    distance = 2
    nameCSV = "nngoog91.csv"
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
    def resetNN(self):
        # ich glaube das geht besser
        if input('resetNN: ') == 'y':
            for i in range(0, self.NNlength):
                for o in range(0, self.NNweigth):
                    self.arrayNN[i][o] = float(random.uniform(-self.distance, self.distance))
            print("done reset NN")

    # gibt einen Layer des NN aus
    def getOneLayer(self, index):
        # wird nur bei layermalweights gebraucht
        theLayer = []
        for i in range(index, index+self.NNweigth):
            theLayer.append(self.arrayNN[i])
        return theLayer

    # matrixmultiplikation speziell für NN-Gewichtungen
    # keine richtige Matrixmultiplikation (nochmal testen)
    def layermalweights(self, layerIn, wightsIn):
        # das ist cool \/
        output = [0] * (self.NNweigth)
        for i in range(0, self.NNweigth):
            for o in range(0, self.NNweigth):
                output[i] = output[i] + (float(layerIn[o]) * float(wightsIn[o][i]))
        return(output)

    # Voraussage nach 10 Tagen (input)
    # Das Neuronale Netz
    def predict(self, daten, show=None):
        output = 0
        # Verarbeitung des Inputs
        for i in range(0, len(daten)):
            if show=="input":
                print(daten[i])
            daten[i] = self.sigmoid(float(daten[i]))
        if show=="input":
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
        output = self.sigmoid(output)
        #print(output)
        return(output)

    # gibt Testergebniss aus
    # wie gut es sich am Kurs geschlagen hat
    def getKnowledge(self, kurs):
        #Zeit
        time = 0
        gesamt = 0
        #gesammt berechnen
        for time in range(10, len(kurs)):
            # Daten für das NN als Eingabelayer sepperiert
            daten = []
            daten = base.seperateData(kurs, time)
            # Berechnung der Vorausagung
            voraussagung = self.predict(daten)
            realesGeschehen = float(kurs[time][0])
            # Berechnung des Gewinns
            gewinn = base.gues(realesGeschehen, voraussagung)
            # lokaler Gewinn wird dem Gesammtgewinn zugerechnet
            gesamt = gesamt + gewinn
        return gesamt

    # Trainiert Neuronales Netz (nur ein neuron)
    def train(self, kurs):
        # Wissensindex vorher
        startKnowledge = self.getKnowledge(kurs)
        #Bestimmen eines Neuronens per zufall
        x = randint(0, len(self.arrayNN)-1)
        y = randint(0, len(self.arrayNN[x])-1)
        # speichern
        save = self.arrayNN[x][y]
        #änderung an dem Neuron vornehmen
        rand = random.uniform(-float(self.distance), float(self.distance))
        self.arrayNN[x][y] = float(self.arrayNN[x][y]) + rand
        # Wissensindex nachher
        newKnowledge = self.getKnowledge(kurs)
        # sollte es sich nicht gebessert haben
        if newKnowledge <= startKnowledge:
            # nimm den alten Wert wieder an
            self.arrayNN[x][y] = save
