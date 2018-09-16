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

# def NN(ENNlayer0, ENNweigths0, ENNweights1, ENNweights2):
#     NNlayer0 = ENNlayer0
#     NNlayer1 = [0, 0, 0]
#     NNlayer2 = [0, 0]
#     NNlayerOut = [0]
#     NNweights0 = ENNweigths0
#     NNweights1 = ENNweights1
#     NNweights2 = ENNweights2
#     NNlayer1 = matmult(NNlayer0, NNweights0, 3, 3)
#     NNlayer2 = matmult(NNlayer1, NNweights1, 3, 2)
#     NNlayerOut = matmult(NNlayer2, NNweights2, 2, 1)
#     return(NNlayerOut)

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
