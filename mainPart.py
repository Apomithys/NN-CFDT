import nnclass
import base
import kursclass
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

learningstats = []

# Einlesen der Kurstabelle
kurs = kursclass.SPkurs()
if input("downloading?: ")=="y":
    kurs.downloadKurs()
kurs.readKurs()
kurs.transformKurs()

# Initialisierung von NeuNet als nnclass Objekt
NeuNet = nnclass.NeuNet("nngoog91.csv")

# Einlesen der CSV für NeuNet
NeuNet.readIn()

# Zurücksetzten den NeuNet
NeuNet.resetNN()

# Trainliere NeuNet
trainlength = int(input("train: "))
for i in range(0, trainlength):
    if(i == 0):
        for i in range(0, trainlength):
            print("#", end="", flush=True)
        print("\n")
    #NeuNet.train(kurs.getAllData(), type="Layer")
    NeuNet.train(kurs.getTrainData(), type="Neuron")
    NeuNet.saveOut()
    learningstats.append(NeuNet.getKnowledge(kurs.getTestData()))
    print("#", end="", flush=True)

plt.plot(learningstats, label="learning")
plt.ylabel('knowledge')
plt.xlabel('time')
plt.show()

# Wissenstand des NeuNet
print("\n" + "wissensindex: " + str(NeuNet.getKnowledge(kurs.getTestData())) + "\n")

# Speichere es in CSV
NeuNet.saveOut()

# Voraussagung
daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-0)
print(NeuNet.predict(daten, chart="input"))