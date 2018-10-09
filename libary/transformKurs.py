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
    #nur wenne es geändert werden muss
    if kurs[0][0] == 'Date':
        newKurs = readTable(nameKurs)

        #tabelle mit 0'en
        #wiederhole für jede zeile, außer header
        for i in range(0, len(newKurs)):
            for o in range(0, len(newKurs[i])):
                newKurs[i][o] = 0
        print(newKurs)

        for i in range(1, len(kurs)-1):
            newKurs[i-1][0] = float(kurs[i+1][4]) - float(kurs[i][4])
        for i in range(1, len(kurs)):
            newKurs[i-1][1] = float(kurs[i][4])
        print(newKurs)
        # die Änderungen von NN werden als .csv gespeichert
        writer = csv.writer(open(nameKurs, 'w', newline=''))
        writer.writerows(newKurs)