import csv

#Einlesen der Tabelle
def readTable(name):
    r = csv.reader(open(name))
    lines = list(r)
    return(lines)

def transformKurs(nameKurs):
    print("start 'transformKurs'")
    #einlesen der tabell in beide Variablen
    kurs = readTable(nameKurs)
    newKurs = readTable(nameKurs)
    #wiederhole für jede zeile, außer header
    for i in range(1, len(newKurs)):
        for o in range(0, len(newKurs[i])):
            newKurs[i][o] = 0
    print(newKurs)
    for i in range(1, len(kurs)):
        newKurs[i][0] = kurs[i][4]
    print(newKurs)
    # die Änderungen von NN werden als .csv gespeichert
    # writer = csv.writer(open('NN.csv', 'w', newline=''))
    # writer.writerows(newKurs)