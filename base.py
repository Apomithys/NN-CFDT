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

# Sepperiert Kursdaten (das muss in kurKlasse rein)
def seperateData(tabelle, t):
    data = [0]*10
    counter = 0
    for p in range(t-10, t):
        data[counter] = tabelle[p][0]
        counter += 1
    return(data)

# Bewertungsfnktion
# real: echter Wert
# x: prediction
def bewertung(real, x):
    maximum = abs(real*real)
    mult = x*real
    if mult>0:
        ausgabe = (-(maximum/(real*real))*(x-real)*(x-real))+maximum
        if ausgabe<0:
            ausgabe = 0
    else:
        ausgabe = mult
    return (ausgabe)