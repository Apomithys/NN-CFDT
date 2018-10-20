import csv
import funktions

def transformKurs(nameKurs):
    #einlesen der tabell in beide Variablen
    kurs = funktions.readTable(nameKurs)
    #nur wenne es geändert werden muss
    if kurs[0][0] == 'Date':
        print("start 'transformKurs'")
        newKurs = funktions.readTable(nameKurs)

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