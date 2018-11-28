import nnclass
import base
import kursclass
import matplotlib.pyplot as plt
learningstats = []

# Einlesen der Kurstabelle
kurs = kursclass.SPkurs()
if input("downloading?: ")=="y":
    kurs.downloadKurs()
kurs.readKurs()
kurs.transformKurs()

# Initialisierung von NeuNet als nnclass Objekt
NeuNet = nnclass.NeuNet()

# Einlesen der CSV für NeuNet
NeuNet.readIn()

# Zurücksetzten den NeuNet
NeuNet.resetNN()

# Letzten 10 Tage des Kurses --> Daten
daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-0)

# Trainliere NeuNet
trainlength = int(input("train: "))
for i in range(0, trainlength):
    if(i == 0):
        for i in range(0, trainlength):
            print("#", end="", flush=True)
        print("\n")
    NeuNet.train(kurs.getAllData())
    learned = NeuNet.getKnowledge(kurs.getTestData())
    learningstats.append(learned)
    print("#", end="", flush=True)

plt.plot(learningstats)
plt.ylabel('some numbers')
plt.show()

# Wissenstand des NeuNet
print("\n" + "wissensindex: " + str(NeuNet.getKnowledge(kurs.getTestData())) + "\n")

# Speichere es in CSV
NeuNet.saveOut()

# Voraussagung
daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-0)
print(NeuNet.predict(daten, show="input"))