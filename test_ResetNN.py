import nnclass
import kursclass
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

resetNNknow = []

# Einlesen der Kurstabelle
kurs = kursclass.SPkurs()
kurs.readKurs()
kurs.transformKurs()

# Initialisierung von NeuNet als nnclass Objekt
NeuNet1 = nnclass.NeuNet("trainingsnn1.csv")

# Einlesen der CSV für NeuNet
NeuNet1.readIn()

# Trainliere NeuNet
trainlength = int(input("test: "))
for i in range(0, trainlength):
    if i == 0:
        for i in range(0, trainlength):
            print("#", end="", flush=True)
        print("\n")
    NeuNet1.resetNN(ask=False)
    resetNNknow.append(NeuNet1.getKnowledge(kurs.getTrainData()))
    print("#", end="", flush=True)

plt.plot(resetNNknow)
plt.ylabel('knowledge')
plt.show()
