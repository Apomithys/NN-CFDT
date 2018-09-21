#Status
print("start test.py")

#Matrixmultiplikation layer * weights mit layer hat länge Lfron und gibt layerB mit Lto länge aus
def matmult(MMlayer, MMweights, MMLfrom, MMLto):
    MMlayerOut = [0, 0]
    for i in range(0, MMLfrom):
        for o in range(0, MMLto):
            MMlayerOut[o] = MMlayerOut[o] + (MMlayer[i] * MMweights[o][i])
    return(MMlayerOut)
    #Status
    print("Matrixmultiplikation erfolgreich berechnet")

a = int(input("0: "))
b = int(input("1: "))
c = int(input("2: "))
layer0 = [ a, b, c]

#gewichtungen zwischen layer0 und layer1
weights0 = [3, 3, 3], [4, 4, 4]
# weights1 = [1, 1, 1], [2, 2, 2]
# weights2 = [5, 5]
# layerOut = NN(layer0, weights0, weights1, weights2)

#Berechnung des usgabelayers
layer1 = matmult(layer0, weights0, 3, 2)
print(layer1)
