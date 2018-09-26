

########################################################   Funktions

#Einlesen der Tabelle
def readTable(name):

    #einlesen der Datei
    dateihandler = open(name)

    #inhalt ist langer String
    inhalt = dateihandler.read()

    #tabelle ist leere liste
    tabelle = []

    #in zeilen aufspalten
    zeilen = inhalt.split('\n')

    #in spalten aufspalten
    for i in range(len(zeilen)):
        spalten = zeilen[i].split(',')
        tabelle.append(spalten)

    #Strings umwandeln in Real
    for i in range(len(tabelle)-1):
        for o in range(len(tabelle[0])):
            tabelle[i][o] = float(tabelle[i][o])

    #ausgebe
    #print(tabelle)
    return(tabelle)

#Kurswette dass bit nach wette ausfällt
def gues(bit, wette):
    #folgene Zeile aukommentieren wenn NN benutzt wird, dann eingabe durch funktion
    wette = float(input("gues: "))
    winn = wette*bit
    return(winn)

#seperate the data für das Netztwerk als output
def seperateData(tabelle, t):
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    for p in range(t-10, t):
        print(tabelle[p][1])
        data[counter] = tabelle[p][1]
        counter = counter + 1
    return(data)

#Einlesen der Tabelle "kurs.csv" als kurs
kurs = []
kurs = readTable("kurs.csv")



########################################################   Network funktion

#Status
print("start test.py")

# #Matrixmultiplikation layer * weights mit layer hat länge Lfron und gibt layerB mit Lto länge aus
# def matmult(MMlayer, MMweights, MMLfrom, MMLto):
#     MMlayerOut = [0, 0]
#     for i in range(0, MMLfrom):
#         for o in range(0, MMLto):
#             MMlayerOut[o] = MMlayerOut[o] + (MMlayer[i] * MMweights[o][i])
#     return(MMlayerOut)
#     #Status
#     print("Matrixmultiplikation erfolgreich berechnet")
#
# #eingabe
# a = int(input("0: "))
# b = int(input("1: "))
# c = int(input("2: "))
# layer0 = [ a, b, c]
#
# #gewichtungen zwischen layer0 und layer1
# weights0 = [3, 3, 3], [4, 4, 4]
#
# #Berechnung des asgabelayers
# layer1 = matmult(layer0, weights0, 3, 2)
#
# #ausgabe
# print(layer1)



########################################################   Main part

money = 10

#Zeit
time = 0
for time in range(10, len(kurs)-1):
    daten = []
    daten = seperateData(kurs, time)
    print("time: " + str(time))
    #Berechnung des wettabfalls
    wettabfall = gues(float(kurs[time][1]), 0)
    print(str(money) + " + " + str(wettabfall))
    #Anrechnug ans Konto
    money = money + wettabfall
    print("= " + str(money))
    print()
