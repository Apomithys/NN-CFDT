import trainNNday
import trainNNyear
import funktions

print("start 'main'")
nameKurs = str(input("kurstabelle: "))
nameNN = str(input("NNtabelle: "))
index = int(input("hidden layer: "))
distance = 2
print()

print("start 'transformKurs'")
funktions.transformKurs(nameKurs)
print()

if str(input("NN zurücksetzen?: "))=="y":
    print("start 'randomizeNN'")
    funktions.randomizeNN(nameNN, index, distance)
    print()

print("start 'dauertestNN'")
funktions.useGetGesamt(nameKurs, nameNN)
print()

# print("start 'trainNNday'")
# trainNNday.trainNNday(nameKurs, nameNN, distance)
# print()

print("start 'trainNNyear'")
trainNNyear.trainNNyear(nameKurs, nameNN, float(distance))
print()

print("start 'dauertestNN'")
funktions.useGetGesamt(nameKurs, nameNN)
print()

print("start 'triffLiveVoraussage'")
funktions.triffLiveVoraussage(nameKurs, nameNN)
print()
print("process ended")
