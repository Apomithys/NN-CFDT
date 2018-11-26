import nnclass
import base
import kursclass

# Einlesen der Kurstabelle
kurs = kursclass.SPkurs()
kurs.downloadKurs()
kurs.readKurs()
kurs.transformKurs()

# Initialisierung von NeuNet als nnclass Objekt
NeuNet = nnclass.NeuNet()

# Einlesen der CSV für NeuNet
NeuNet.readIn()

# Zurücksetzten den NeuNet
NeuNet.resetNN()

# Wissenstand des NeuNet
print(NeuNet.getKnowledge(kurs.getTestData()))

# Letzten 10 Tage des Kurses --> Daten
daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-0)

# Triff Voraussagung nach Daten
print("prediction: " + str(NeuNet.predict(daten)))

# Trainliere NeuNet
NeuNet.train(kurs.getTrainData(), int(input("train: ")), timestat=True)

# Wissenstand des NeuNet
print("\n" + "wissenstand: " + str(NeuNet.getKnowledge(kurs.getTestData())) + "\n")

# Speichere es in CSV
NeuNet.saveOut()

# Voraussagung
daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-0)
print(NeuNet.predict(daten, show="input"))