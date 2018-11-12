#importiert die Funktionen
import funktions
import base

#eingabe
print("start 'main'")
#name der Tabelle in der die historischen Kursdaten liegen
nameKurs = str(input("kurstabelle: "))
#name der Datei in der das NN gespeichert werden soll
nameNN = str(input("NNtabelle: "))

#gewichtung den die Synapsen maximal haben
synDistance = 2
print()

#setzt das NN zurück
#base.randomizeNN(nameNN, 10, synDistance)

#formartiert die datei mit den historischen Kursdaten
print("start 'transformKurs'")
funktions.transformKurs(nameKurs)
print()

#liest die Tabellen ein
kurs = base.readTable(nameKurs)
NeuNet = base.readTable(nameNN)

#gibt den Gewinn des NN au sden es am Markt machen würde
#bzw. wie oft es richtig lag
print("start 'getGesamt'")
print(str(funktions.getGesamt(kurs, NeuNet)))
print()

inp = str(input("what do you want? "))
if inp=="layer":
    print("start 'trainNNlayer'")
    NeuNet = funktions.trainNNlayer(kurs, NeuNet, float(synDistance))
    print()
elif inp=="neuron":
    print("start 'trainNNneuron'")
    NeuNet = funktions.trainNNneuron(kurs, NeuNet, float(synDistance))
    print()
else:
    print("pass")

base.saveArray(NeuNet, nameNN)


print("start 'getGesamt'")
print(str(funktions.getGesamt(kurs, NeuNet)))
print()

print("start 'triffLiveVoraussage'")
funktions.triffLiveVoraussage(nameKurs, nameNN)

print()
print("process ended")
