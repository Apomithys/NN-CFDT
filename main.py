import randomizeNN
import trainNNday
import trainNNyear
import dauertestNN
import transformKurs
import NN_CFDT

nameKurs = str(input("kurstabelle: "))
nameNN = str(input("NNtabelle: "))
index = int(input("hidden layer: "))
distance = float(input("range NN: "))
print()

transformKurs.transformKurs(nameKurs)
print()

if str(input("wilst du das NN randomizen?: "))=="True":
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
trainNNyear.trainNNyear(nameKurs, nameNN, float(distance)/2)
print()

print("start 'dauertestNN'")
dauertestNN.dauertestNN(nameKurs, nameNN)
print()

print("start 'triffVoraussage'")
NN_CFDT.triffVoraussage(nameKurs, nameNN)
print()
