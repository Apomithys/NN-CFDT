#import stuff
print("importing stuff...")
import base
import random
from random import randint
import math


class NeuNet:
    
    knowledge = 0
    arrayNN = []
    NNlength = 100
    NNweigth = 10
    distance = 2
    nameCSV = "nngoog91.csv"

    #sigmoud funktion
    #nicht wirklich (nur vrearbeitung des Inputs)
    def sigmoid(self, x):
        # sigmoid Funktion
        out = (((1 / (1 + math.exp(-(x))))-0.5)*2)
        # Ausgabe
        return out

    # Einlesen des NN aus einer CSV
    def readIn(self):
        self.arrayNN = base.readTable(self.nameCSV)
    
    # Exportieren des NN in eine CSV
    def saveOut(self):
        base.saveArray(self.arrayNN, self.nameCSV)

    # Setzt NN zurück
    def resetNN(self):
        if input('resetNN: ') == 'y':
            for i in range(0, self.NNlength):
                for o in range(0, self.NNweigth):
                    self.arrayNN[i][o] = float(random.uniform(-self.distance, self.distance))
            print("done reset NN")

    # Zieht einen Layer des NN
    def getOneLayer(self, index):
        theLayer = []
        for i in range(index, index+self.NNweigth):
            theLayer.append(self.arrayNN[i])
        return theLayer

    # matrixmultiplikation speziell für NN-Gewichtungen
    # keine richtige Matrixmultiplikation
    # sollte nicht in main benutz werden
    def layermalweights(self, layerIn, wightsIn):
        output = [0] * (self.NNweigth)
        for i in range(0, self.NNweigth):
            for o in range(0, self.NNweigth):
                output[i] = output[i] + (float(layerIn[o]) * float(wightsIn[o][i]))
        #ausgabe des outputlayers
        return(output)

    # Voraussage nach 10 Tagen (input)
    def predict(self, daten, show=None):
        output = 0
        #Input wird verarbeitet
        for i in range(0, len(daten)):
            if show=="input":
                print(daten[i])
            daten[i] = self.sigmoid(float(daten[i]))
        if show=="input":
            print()    
        #layer 1 wird geleert
        layer1 = [0] * (self.NNweigth)
        #vom input zum layer 1 gerechnet (1. hidden layer)
        wigthsLayer = self.getOneLayer(0)
        layer1 = self.layermalweights(daten, wigthsLayer)
        #wiederholt für jeden weiteren hidden layer 
        # einen hat es schon gemacht
        # arbeitet sich für jeden layer weiter
        for i in range(self.NNweigth, self.NNlength, self.NNweigth):
            #layer2 wird geleert und berechnet mit layer1
            layer2 = [0] * (self.NNweigth)
            wigthsLayer = self.getOneLayer(i)
            layer2 = self.layermalweights(layer1, wigthsLayer)
            #ergebniss wird an layer 1 weiter gegeben
            for o in range(0, self.NNweigth):
                #ausgabe wird verarbeitet
                layer1[o] = self.sigmoid(layer2[o])
            #so ergibt sich eine Scheife die es möglich mach unenlich lange NN zu bauen
        for o in range(0, self.NNweigth):
            #output darf nur ein wert sein
            pass
            output = output + layer1[o]
        #output wird noch einmal bearbeitet
        #aber nur der eine wert
        #also der letzte Layer
        output = self.sigmoid(output)
        #ausgabe
        #print(output)
        return(output)

    # gibt Testergebniss an Kurs aus
    def getKnowledge(self, kurs):
        #Zeit
        time = 0
        gesamt = 0
        #gesammt berechnen
        for time in range(10, len(kurs)):

            #sichtbare Daten für das NN als Eingabelayer werden sepperiert
            daten = []
            daten = base.seperateData(kurs, time)

            #Berechnung der Vorausagung
            voraussagung = self.predict(daten)
            realesGeschehen = float(kurs[time][0])

            #Berechnung des gewinns
            gewinn = base.gues(realesGeschehen, voraussagung, nominus=True)

            #gewinn wird dem gesammtgewinn zugerechnet
            gesamt = gesamt + gewinn
        self.knowledge = gesamt
        return self.knowledge

    # Trainiert NN (neuron)
    def train(self, kurs, counter, timestat=False, trainingstat=False):
        startKnowledge = self.getKnowledge(kurs)
        
        lastLoadBlock = 0
        #wiedeholung bis counter
        for i in range(1, counter):
            if timestat!=False:
                lastLoadBlock+=1
                if (lastLoadBlock>counter/55):
                    print ('█', end="", flush=True)
                    lastLoadBlock = 0
            #Bestimmen der Neuronenreihe per zufall
            x = randint(0, len(self.arrayNN)-1)
            y = randint(0, len(self.arrayNN[x])-1)

            #sichern damit nichts kaputt geht
            save = 0
            save = self.arrayNN[x][y]

            #änderung an dem Neuron
            rand = random.uniform(-float(self.distance), float(self.distance))
            self.arrayNN[x][y] = float(self.arrayNN[x][y]) + rand

            #ermitteln des neuen gewinns nach der Änderung
            newKnowledge = self.getKnowledge(kurs)
                    
            #wenn es schlechter geworden ist
            if newKnowledge <= startKnowledge:
                #nimm das alte
                self.arrayNN[x][y] = save
            else:
                #wissenstand neu
                startKnowledge = newKnowledge
                #wenn es besser geworden ist belasse es dabei
                if trainingstat!=False:
                    print()
                    print(str(i) + " / " + str(counter-1))
                    print("gesammt: " + str(newKnowledge))

                    print()
