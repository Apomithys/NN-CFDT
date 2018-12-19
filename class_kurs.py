#import stuff
import base
import datetime
import pandas_datareader as web
from array import *


class SPkurs:
    # Rohe Daten von der Yahoo API
    rawData = []
    # schon verarbeitete Daten (desamte Historie)
    allData = []
    # schon verarbeitete Daten (Trainingsdaten)
    trainData = []
    # schon verarbeitete Daten (Testdaten)
    testData = []
    # Tag des Stocks
    kursIdx = "goog"

    # Liest Kursdaten aus CSV aus
    def readKurs(self):
        pass
        self.rawData = base.readTable(str(self.kursIdx)+".csv")

    # Speichert Kurs als CSV
    def saveKurs(self):
        pass
        base.saveArray(self.rawData, str(self.kursIdx)+".csv")

    # Lädt historische Kursdaten herunter
    def downloadKurs(self):
        pass
        print("downloading...")
        # Lädt Daten herunter
        newData = web.get_data_yahoo(str(self.kursIdx))
        # Speichert Array als CSV
        newData.to_csv(path_or_buf=str(str(self.kursIdx)+".csv"))
        # Liest Daten aus CSV ein
        self.readKurs()

    # Formatiert rohe Kursdaten von API
    def transformKurs(self, traintestverhalt=110, datensatzgroesse=510):
        # Einlesen der CSV
        newKurs = base.readTable(str(self.kursIdx)+".csv")
        # Länge des Arrays
        kurstiefe = len(newKurs)
        # Breite des Arrays
        kursbreite = len(newKurs[0])
        # Tabelle mit 0'en erstellen
        # Das muss besser gehen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Allgemein dieses komische hin und her packen...
        for i in range(0, kurstiefe):
            for o in range(0, kursbreite):
                newKurs[i][o] = 0
        # newKurs = [[0]*kursbreite]*kurstiefe
        # Prozentualer Anstieg des Kurses von jedem Tag wrird berechnet
        for i in range(1, kurstiefe-1):
            # Wert des Vortages: float(kurs[i][4])
            # Wert des jetzigen Tages: float(kurs[i+1][4])
            newKurs[i-1][0] = ((float(self.rawData[i+1][4])/float(self.rawData[i][4]))-1)*100
        for i in range(1, kurstiefe):
            newKurs[i-1][1] = float(self.rawData[i][4])
        for i in range(0, kurstiefe):
            del newKurs[i][6]
            del newKurs[i][5]
            del newKurs[i][4]
            del newKurs[i][3]
            del newKurs[i][2]
        del newKurs[kurstiefe-1]
        del newKurs[kurstiefe-2]
        kurstiefe=kurstiefe-2
        # Reduziert die Tabelle auf die letzten 500 Tage
        while kurstiefe>datensatzgroesse:
            del newKurs[0]
            kurstiefe=kurstiefe-1
        for i in range(0, kurstiefe):
            del newKurs[i][1]
        # allData enthällt die verarbeiteten Daten vonn 500 Tagen
        self.allData = newKurs
        print("Kursdatei formatiert")

        # Aufteilen der Daten in train und testData
        self.trainData = list(self.allData)
        self.testData = list(self.allData)
        # testData sind die letzten 100 Tage
        for i in range(0, len(self.allData)-traintestverhalt):
            del self.testData[0]
        # trainData sind alle anderen Daten
        for i in range(len(self.allData), (len(self.allData)-traintestverhalt), -1):
           del self.trainData[i-1]

    # Gibt Kursdaten zum Testen eines NN aus
    def getTestData(self):
        return self.testData
    
    # Gibt Kursdaten zum Trainieren eines NN aus
    def getTrainData(self):
        return self.trainData
    
    # Gibt alle Kursdaten aus
    def getAllData(self):
        return self.allData