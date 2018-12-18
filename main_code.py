import base
import class_kurs
import class_nn
import matplotlib.pyplot as plt
from matplotlib import style
import time
from tqdm import tqdm

style.use('fivethirtyeight')

learningstats = []

# Einlesen der Kurstabelle
kurs = class_kurs.SPkurs()
if input("downloading?: ")=="y":
    kurs.downloadKurs()
kurs.readKurs()
kurs.transformKurs()

# Initialisierung von NeuNet als nnclass Objekt
NeuNet = class_nn.NeuNet("nngoog91.csv")

# Einlesen der CSV für NeuNet
NeuNet.readIn()

# Zurücksetzten den NeuNet
NeuNet.resetNN()

# Trainliere NeuNet
trainlength = int(input("how many iterations: "))
start = time.time()
counter=0
for i in tqdm(range(trainlength)):
    counter+=1
    #NeuNet.train(kurs.getAllData(), type="Layer")
    NeuNet.train(kurs.getTrainData(), type="Neuron")
    learningstats.append(NeuNet.getKnowledge(kurs.getTestData()))
    if (counter%25)==0:
        NeuNet.saveOut()

plt.plot(learningstats, label="learning")
plt.ylabel('knowledge')
plt.xlabel('time')
plt.legend()
plt.show()

# Wissenstand des NeuNet
print("\n" + "wissensindex: " + str(NeuNet.getKnowledge(kurs.getTestData())) + "\n")

# Speichere es in CSV
NeuNet.saveOut()

voraussagungen=[]
# Voraussagung
for i in range(10, 0, -1):
    daten = base.seperateData(kurs.getAllData(), len(kurs.getAllData())-i)
    voraussagungen.append(NeuNet.predict(daten))
plt.plot(voraussagungen, label='Voraussagungen', marker='o')
plt.plot(daten, label='echte Daten')
plt.legend()
plt.show()