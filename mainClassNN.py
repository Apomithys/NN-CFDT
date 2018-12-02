import nnclass
import base
import kursclass
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

learningstats = []
visuallearn = []

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

# Letzten 10 Tage des Kurses --> Daten
daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-0)

# Trainliere NeuNet
trainlength = int(input("train: "))
for i in range(0, trainlength):
    if(i == 0):
        for i in range(0, trainlength):
            print("#", end="", flush=True)
        print("\n")
    #NeuNet.train(kurs.getAllData(), type="Layer")
    NeuNet.train(kurs.getAllData(), type="Neuron")
    NeuNet.saveOut()
    learned = NeuNet.getKnowledge(kurs.getTestData())
    visuallearn.append(NeuNet.getKnowledge(kurs.getTrainData()))
    learningstats.append(learned)
    print("#", end="", flush=True)

plt.plot(learningstats)
plt.plot(visuallearn)
plt.ylabel('knowledge')
plt.show()

# Wissenstand des NeuNet
print("\n" + "wissensindex: " + str(NeuNet.getKnowledge(kurs.getTestData())) + "\n")

# Speichere es in CSV
NeuNet.saveOut()

# Voraussagung
daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-0)
print(NeuNet.predict(daten, chart="input"))