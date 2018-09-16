#Status
print("start test.py")

#Matrixmultiplikation layer * weights mit layer hat länge Lfron und gibt layerB mit Lto länge aus
def matmult(layer, weights, Lfrom, Lto):
    layerB = [0, 0]
    for i in range(0, Lfrom):
        for o in range(0, Lto):
            layerB[o] = layerB[o] + (layer[i] * weights[o][i])
    return(layerB)
    #Status
    print("Matrixmultiplikation erfolgreich berechnet")

#eingabelayer
a = int(input("0: "))
b = int(input("1: "))
c = int(input("2: "))
layer0 = [ a, b, c]

#gewichtungen zwischen layer0 und layer1
weights0 = [ 3, 3, 3],[ 4, 4, 4]

#Berechnung des usgabelayers
layer1 = matmult(layer0, weights0, 3, 2)
