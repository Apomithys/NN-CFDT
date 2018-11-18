import nnclass
import base
import kursclass

# Einlesen der Kurstabelle
kurs = kursclass.SPkurs()
kurs.readKurs("goog.csv")
kurs.transformKurs()

# Initialisierung von NeuNet als nnclass Objekt
NeuNet = nnclass.NeuNet()

# Einlesen der CSV für NeuNet
NeuNet.readIn("nngoog91.csv")

# Zurücksetzten den NeuNet
NeuNet.resetNN()

# Wissenstand des NeuNet
print(NeuNet.getKnowledge(kurs.kursArray))

# Letzten 10 Tage des Kurses --> Daten
daten = base.seperateData(kurs.kursArray, len(kurs.kursArray)-0)

# Triff Voraussagung nach Daten
print(NeuNet.predict(daten))

# Trainliere NeuNet
NeuNet.train(kurs.kursArray, int(input("train: ")))

# Wissenstand des NeuNet
print("\n" + str(NeuNet.getKnowledge(kurs.kursArray)))

# Speichere es in CSV
NeuNet.saveOut("nngoog91.csv")

daten = base.seperateData(kurs.kursArray, len(kurs.kursArray)-0)
print(NeuNet.predict(daten))