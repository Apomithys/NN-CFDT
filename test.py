from libary import randomizeNN
from libary import trainNNday
from libary import dauertestNN
from libary import transformKurs
from libary import NN_CFDT

nameKurs = str(input("kurstabelle: "))
nameNN = str(input("NNtabelle: "))

#transformKurs.transformKurs()
randomizeNN.randomizeNN(nameNN)
trainNNday.trainNNday(nameKurs, nameNN)
dauertestNN.dauertestNN(nameKurs, nameNN)
NN_CFDT.triffVoraussage(nameKurs, nameNN)