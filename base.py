import random
from random import randint
import time
import csv
import math

# Einlesen einer CSV
def readTable(name):
    r = csv.reader(open(name))
    lines = list(r)
    return(lines)

# Speichern eines Arrays in CSV
def saveArray(array, csvname):
    writer = csv.writer(open(str(csvname), 'w', newline=''))
    writer.writerows(array)

# Sepperiert Kursdaten
def seperateData(tabelle, timing):
    data = [0]*10
    counter = 0
    for p in range(timing-10, timing):
        data[counter] = tabelle[p][0]
        counter += 1
    # Gibt 10 letzten Werte nach 'timing' aus
    return(data)

# Bewertungsfnktion
# real: echter Wert
# prediction: Voraussagung
def bewertung(real,  prediction):
    maximum = abs(real*real)
    mult = prediction*real
    if mult>0:
        ausgabe = (-(maximum/(real*real))*(prediction-real)*(prediction-real))+maximum
        if ausgabe<0:
            ausgabe = 0
    else:
        ausgabe = mult
    return (ausgabe)