# NN-CFDT

Dieses Projekt unterliegt der MIT-Lizenz.

## Neural Network

Dieses Programm ist ein Neuronales Netz (NN), welches den zukünftigen Verlauf eines CSV (comma separates values) Datensatzes voraussagen soll. In jeglicher Hinnsicht ist keine Gewähr oder Haftung gegeben.
Es ist in Python geschrieben. Ich habe darauf geachtet möglichst wenige Bibliotheken zu verwenden. Aus dem einfachen Grud, dass dieses Projekt hauptsächlich dazu da ist, dass ich selbst meine "Programmier Skills" verbessere und NN's, ML (machine learning) und Python besser verstehe. 

## Documentation

### class NeuNet:

Eine Instanz der Klasse NeuNet stellt ein Neuronales Netz dar. Die Funktionen des Neronalen Netztes werden im Folgenden erklärt.
Um diese Klasse zu nutzen muss am Anfang des Codes das richtige File importiert werden.
'''
import nnclass
'''
oder 
'''
from nnclass import NeuNet
'''

#### Einlesen und Exportieren

Um das Neuronale Netz weiter zu entwickeln ist es nützlich das NN irrendwie speichern und einlesen zu können. Es gibt Funktionen, die es ermöglichen das NN als .CSV Datei ab zu speichern, um es später wieder einlesen zu können.

Folgende Funktion macht es möglich ein bereits Vorhandenes NN aus einer .CSV ein zu lesen.
'''
.readIn()
'''

Folgende Funktion macht es möglich ein neues NN in eine .CSV zu exportieren.
'''
.saveOut()
'''

Es besteht auch die Möglchkeit das NN wieder zurück zu setzen. Dabei wird das gesamte NN überschrieben. Aus Sicherheitsgründen wird der Benutzer vorher gefragt ob es wirklich gewollt ist, das NN zurück zu setzen. Mit folgender Funktion wird das NN zurück gesetzt.
'''
.resetNN()
'''


#### Verwendung des NN

Ein NN dient dazu, eine Voraussagung zu treffen. Wie ein NN funktioniert ist sehr interessant, wird hier allerding nicht erklärt. In dem [Wikipedia Artikel](https://de.wikipedia.org/wiki/K%C3%BCnstliches_neuronales_Netz) wird die Funktionsweise eines NN sehr gut beschrieben.

Um eine Voraussagung zu treffen sollte einfach folgende Funktion verwendet werden.
'''
.predict(daten, show=None)
'''
>daten: ein Array welches genau so lang sein sollte wie das NN breit ist (INPUT)
>show: (None/input) präsentiert den Input des NN, oder eben nicht.
Diese Funktion gibt einen Wert zurück. Dieser ist die Voraussagung.

Ein untrainirtes NN gibt nur unfug aus. Deswegen hat die Klasse auch eine Funktion mit der das NN auch trainiert werden kann. Es gibt unterschiedliche Methoden wie man ein NN trainieren kann. Das "Lernen" was in der Funktion passiert ist auch kein bekannter bzw. oft genutzter Algorithmus. Die Idee liegt darin, dass zu Beginn getestet wird, wie gut das NN bereits ist. Anschließend wird eine willkürliche/zufällige Änderung an dem NN vorgenommen. Dadurch ändert sich die Art und Weise, wie das NN auf Input reagiert. So ändert sich auch das Können des NN. Also wird, nach der Änderung, das NN nochmal getestet. Daraufhin wird verglichen, ob die Änderung positive oder negative Auswirkungen auf das Verhalten des NN genommen hat. Sollte es sich gebessert haben, so wird die Änderung gespeichert.
Der Trainings-Befehl lautet:
'''
.train(kurs, type=None)
'''
>type: (Neuron/Layer) Trainingsmodus.
>kurs: Datensatz an dem trainiert weren soll.
