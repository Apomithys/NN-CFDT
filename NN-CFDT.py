# #Status
# print("start test.py")
#
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

money = 100

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

def gues(bit):
    gues = float(input("gues: "))
    money = money + gues*bit
    print("you get: " + str(gues*bit))
    print("You have now: " + str(money))

kurs = []
kurs = readTable("kurs.csv")

gues(kurs[0][0])
