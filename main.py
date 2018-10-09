from libary import randomizeNN
from libary import trainNNday
from libary import trainNNyear
from libary import dauertestNN
from libary import transformKurs
from libary import NN_CFDT

nameKurs = str(input("kurstabelle: "))
nameNN = str(input("NNtabelle: "))
index = int(input("hidden layer: "))
distance = float(input("range NN: "))
print()

transformKurs.transformKurs(nameKurs)
print()

if bool(input("wilst du das NN randomizen?: "))==True:
    print("start 'randomizeNN'")
    randomizeNN.randomizeNN(nameNN, index, distance)
    print()

print("start 'dauertestNN'")
dauertestNN.dauertestNN(nameKurs, nameNN)
print()

# print("start 'trainNNday'")
# trainNNday.trainNNday(nameKurs, nameNN, distance)
# print()

print("start 'trainNNyear'")
trainNNyear.trainNNyear(nameKurs, nameNN, float(distance)*2)
print()

print("start 'dauertestNN'")
dauertestNN.dauertestNN(nameKurs, nameNN)
print()

print("start 'triffVoraussage'")
NN_CFDT.triffVoraussage(nameKurs, nameNN)
print()
