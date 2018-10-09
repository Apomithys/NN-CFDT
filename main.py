from libary import randomizeNN
from libary import trainNNday
from libary import trainNNyear
from libary import dauertestNN
from libary import transformKurs
from libary import NN_CFDT

nameKurs = str(input("kurstabelle: "))
nameNN = str(input("NNtabelle: "))
index = int(input("hidden layer: "))
print()

transformKurs.transformKurs(nameKurs)
print()

if bool(input("wilst du das NN randomizen?: "))==True:
    print("start 'randomizeNN'")
    randomizeNN.randomizeNN(nameNN, index)
    print()

print("start 'dauertestNN'")
dauertestNN.dauertestNN(nameKurs, nameNN)
print()

# print("start 'trainNNday'")
# trainNNday.trainNNday(nameKurs, nameNN)
# print()

print("start 'trainNNyear'")
trainNNyear.trainNNyear(nameKurs, nameNN)
print()

print("start 'dauertestNN'")
dauertestNN.dauertestNN(nameKurs, nameNN)
print()

print("start 'triffVoraussage'")
NN_CFDT.triffVoraussage(nameKurs, nameNN)
print()