import random
from random import randint
import time
import csv
import math

#Einlesen einer Tabelle (.csv)
def readTable(name):
    #funktioneiert!
    #nicht berühren!!!!!!!!!
    #einlesen
    r = csv.reader(open(name))
    #auflisten
    lines = list(r)
    #ausgabe
    return(lines)

#speichert das NN in ein .csv File
def saveArray(array, csvname):
    writer = csv.writer(open(str(csvname), 'w', newline=''))
    writer.writerows(array)

#schneidet den Sichtbereich für das Netztwerk zu
#da das NN nur die letzten 10 tage sehen soll
def seperateData(tabelle, t):
    #tabelle ist die kustabelle
    #t ist die Zeit (0 heißt Live-Voraussage)
    #letzten 10 Tage
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #
    counter = 0
    #von tag 10 zu tag 0
    for p in range(t-10, t):
        #counter muss immer zwischen 0 und 10 sein
        #p allerdings ziemlich hoch
        #also gibt es 2 zählervariablen
        data[counter] = tabelle[p][0]
        #counter ist 2. zählervariable
        counter += 1
    #ausgabe der daten
    return(data)

#wetten, dass "nach" neu die "wette" eintritt
def gues(neu, wette, nominus=False):
    #binäre Variante
    out = 0
    zwi = neu * wette
    if zwi > 0:
        out = 1
    elif zwi < 0:
        if nominus==False:
            out = -1
    return(out)
