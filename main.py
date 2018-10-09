from libary import randomizeNN
from libary import trainNNday
from libary import trainNNyear
from libary import dauertestNN
from libary import transformKurs
from libary import NN_CFDT

nameKurs = str(input("kurstabelle: "))
nameNN = str(input("NNtabelle: "))
index = int(input("radikal?: "))

transformKurs.transformKurs(nameKurs)
randomizeNN.randomizeNN(nameNN, index)
dauertestNN.dauertestNN(nameKurs, nameNN)
#trainNNday.trainNNday(nameKurs, nameNN)
trainNNyear.trainNNyear(nameKurs, nameNN)
dauertestNN.dauertestNN(nameKurs, nameNN)
NN_CFDT.triffVoraussage(nameKurs, nameNN)