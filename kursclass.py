#import stuff
import base
import random
from random import randint


class SPkurs:

    kursArray = []

    def readKurs(self, nameCSV):
        self.kursArray = base.readTable(nameCSV)

    #formartiert die .csv Datei mit den Kursdaten für das Programm
    #schneidet es außerdem auf 100 Tage zu
    def transformKurs(self):
        #nur wenne es geändert werden muss
        if self.kursArray[0][0] == 'Date':
            #print("start 'transformKurs'")
            newKurs = self.kursArray
            #größer der Tabelle 
            #spart Zeit auch für die Scheifen
            lengthx = len(newKurs)
            lengthy = len(newKurs[0])
            #tabelle mit 0'en erstellen
            #das muss besser gehen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #wiederhole für jede zeile und Spalte
            for i in range(0, lengthx):
                for o in range(0, lengthy):
                    #setzte es auf null
                    newKurs[i][o] = 0
            #print(newKurs)
            #steigung wrird berechnet und in 0 gepackt
            for i in range(1, lengthx-1):
                #das ist der wichtige Stuff!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #formel so umstellen dass der Prozentuale Anstieg berechnet wird
                #alter Wert: float(kurs[i][4])
                #neuerer Wert: float(kurs[i+1][4])
                #newKurs[i-1][0] = float(kurs[i+1][4]) - float(kurs[i][4])
                newKurs[i-1][0] = ((float(self.kursArray[i+1][4])/float(self.kursArray[i][4]))-1)*100
            #packt die daten von 4 zu 1
            for i in range(1, lengthx):
                newKurs[i-1][1] = float(self.kursArray[i][4])
            #löscht die letzten spalten mit nullen
            for i in range(0, lengthx):
                del newKurs[i][6]
                del newKurs[i][5]
                del newKurs[i][4]
                del newKurs[i][3]
                del newKurs[i][2]
            #print(newKurs)
            #lösche die letzten beiden zeilen
            #ertse war mal die 1. Zeile (hedder)
            del newKurs[lengthx-1]
            #zweite war die letzte die übrich bleibt beim berechnen der differenz der zeiten...
            del newKurs[lengthx-2]
            lengthx=lengthx-2
            #reduziert die Tabelle auf die letzten 100 Tage
            if lengthx>110:
                while lengthx>110:
                    del newKurs[0]
                    lengthx=lengthx-1
            #löscht die 2. Spalte weil die nicht mehr benötigt wird und nur verwirrt...
            for i in range(0, lengthx):
                del newKurs[i][1]
            
            self.kursArray = newKurs
            print("Kursdatei formatiert")
        else:
            print("Datei ist bereits formatiert")
