import base
import nnclass
import kursclass
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

training1array = []
training2array = []

# Einlesen der Kurstabelle
kurs = kursclass.SPkurs()
kurs.readKurs()
kurs.transformKurs()

# Initialisierung von NeuNet als nnclass Objekt
NeuNet1 = nnclass.NeuNet("trainingsnn1.csv")
NeuNet2 = nnclass.NeuNet("trainingsnn1.csv")

# Einlesen der CSV für NeuNet
NeuNet1.readIn()
NeuNet2.readIn()
training1array.append(NeuNet1.getKnowledge(kurs.getTrainData()))
training2array.append(NeuNet2.getKnowledge(kurs.getTrainData()))

# Trainliere NeuNet
trainlength = int(input("train: "))
for i in range(0, trainlength):
    if i == 0:
        for i in range(0, trainlength):
            print("#", end="", flush=True)
        print("\n")
    NeuNet1.train(kurs.getTrainData(), type="Neuron")
    NeuNet2.train(kurs.getTrainData(), type="Layer")
    training1array.append(NeuNet1.getKnowledge(kurs.getTestData()))
    training2array.append(NeuNet2.getKnowledge(kurs.getTestData()))
    print("#", end="", flush=True)

plt.plot(training1array, label="Neuron")
plt.plot(training2array, label="Layer")
plt.ylabel('knowledge')
plt.xlabel('time')
plt.legend()
plt.show()
