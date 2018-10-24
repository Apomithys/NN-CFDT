'''
Programm NN
Neuronales Netzwerk zum Lernen von Kursänderungen
Ver. 24.10.2018	py3
'''

# import helping functions
import randomizeNN
import trainNNday
import trainNNyear
import dauertestNN
import transformKurs
import NN_CFDT

### Eingaben ###
# Kurstabelle enthält ...
nameKurs = str(input("kurstabelle: "))
# NN-Tabelle
nameNN = str(input("NNtabelle: "))
# Anzahl der Layer
index = int(input("hidden layer: "))
# 
distance = float(input("range NN: "))
#print()

transformKurs.transformKurs(nameKurs)
#print()

if str(input("wilst du das NN randomizen?: "))=="True":
    print("start 'randomizeNN'")
    randomizeNN.randomizeNN(nameNN, index, distance)

print("___________________")

print("start 'dauertestNN'")
dauertestNN.dauertestNN(nameKurs, nameNN)
print()

# print("start 'trainNNday'")
# trainNNday.trainNNday(nameKurs, nameNN, distance)
# print()

print("start 'trainNNyear'")
trainNNyear.trainNNyear(nameKurs, nameNN, float(distance)/2)
print()

print("start 'dauertestNN'")
dauertestNN.dauertestNN(nameKurs, nameNN)
print()

print("start 'triffVoraussage'")
NN_CFDT.triffVoraussage(nameKurs, nameNN)
print()
