import funktions

print("start 'main'")
nameKurs = str(input("kurstabelle: "))
nameNN = str(input("NNtabelle: "))

# #aus Sicherheitsgründen auskommentiert damitt die Datei nicht beschädigt wird...
# index = int(input("hidden layer: "))
index = 10
distance = 2
print()

print("start 'transformKurs'")
funktions.transformKurs(nameKurs)
print()

# #aus Sicherheitsgründen auskommentiert weil ich nun komplett der goog Aktie folge
# if str(input("NN zurücksetzen?: "))=="y":
#     print("start 'randomizeNN'")
#     funktions.randomizeNN(nameNN, index, distance)
#     print()

print("start 'dauertestNN'")
funktions.useGetGesamt(nameKurs, nameNN)
print()

print("start 'trainNNyear'")
funktions.trainNNyear(nameKurs, nameNN, float(distance))
print()

print("start 'dauertestNN'")
funktions.useGetGesamt(nameKurs, nameNN)
print()

print("start 'triffLiveVoraussage'")
funktions.triffLiveVoraussage(nameKurs, nameNN)
print()
print("process ended")
