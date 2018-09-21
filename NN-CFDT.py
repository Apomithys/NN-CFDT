#Status
print("start test.py")

class NN(self):
        def __init__():
            

#Matrixmultiplikation layer * weights mit layer hat länge Lfron und gibt layerB mit Lto länge aus
def matmult(MMlayer, MMweights, MMLfrom, MMLto):
    MMlayerOut = [0, 0]
    for i in range(0, MMLfrom):
        for o in range(0, MMLto):
            MMlayerOut[o] = MMlayerOut[o] + (MMlayer[i] * MMweights[o][i])
    return(MMlayerOut)
    #Status
    print("Matrixmultiplikation erfolgreich berechnet")

#eingabe
a = int(input("0: "))
b = int(input("1: "))
c = int(input("2: "))
layer0 = [ a, b, c]

#gewichtungen zwischen layer0 und layer1
weights0 = [3, 3, 3], [4, 4, 4]

#Berechnung des asgabelayers
layer1 = matmult(layer0, weights0, 3, 2)

#ausgabe
print(layer1)
