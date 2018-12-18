# NN-CFDT

Dieses Projekt unterliegt der MIT-Lizenz.

## Neural Network for Contract For Difference Traiding

Dieses Programm ist ein Neuronales Netz, welches den zukünftigen Kursverlauf von einam bestimmten Wertpapier voraussagen soll.
Es ist in Python geschrieben. Ich habe darauf geachtet möglichst wenige Bibliotheken zu verwenden. Aus dem einfachen Grud, dass dieses Projekt hauptsächlich dazu da ist, dass ich selbst meine "Programmier Skills" verbessere und NN's, ML und Python besser verstehe.

## Documentation

### class NeuNet:

Ein Objekt der Klasse NeuNet ist ein Neuronales Netz. Die Funktionen des Neronalen Netztes werden im Folgenden erklärt.
Um diese Klasse zu nutzen muss am Anfang des Codes das richtige File importiert werden.
'''
import nnclass
'''

#### Einlesen und Exportieren

Um das Neuronale Netz weiter zu entwickeln ist es nützlich das NN irrendwie speichern und einlesen zu können. Es gibt funktionen die es ermöglichen das NN als .CSV Datei ab zu apeichern um es später wieder einlesen zu können.

Folgende Funktion macht es möglich ein bereits Vorhandenes NN aus einer .CSV ein zu lesen.
'''
.readIn()
'''

Folgende Funktion macht es möglich ein neues NN in eine .CSV zu exportieren.
'''
.saveOut()
'''

Es besteht auch die Möglchkeit das NN wieder zurück zu setzten. Dabei wird das gesamte NN über schrieben. Aus Sicherheitsgründen wird der Benutzer vorher gefragt ob es wirklich gewollt ist das NN zurück zu setzten. Mit folgender Funktion wird das NN zurück gesetzt.
'''
.resetNN()
'''

#### Verwendung des NN

Ein NN ist dazu da eine Voraussagung zu treffen. Wie ein NN funktioniert ist sehr interessant, wird hier allerding nicht erklärt. In dem [Wikipedia Artikel](https://de.wikipedia.org/wiki/K%C3%BCnstliches_neuronales_Netz) wird die Funktionsweise eines NN sehr gut beschrieben.

Um eine Voraussagung zu treffen sollte einfach folgende Funktion verwendet werden.
'''
.predict(daten, show=None)
'''
>daten: ein Array welches genau so lang sein sollte wie das NN breit ist (INPUT)
>show: (None/input) präsentiert den Input des NN, oder eben nicht.
Diese Funktion gibt einen Wert zurück. Dieser ist die Voraussagung.

Ein untrainirtes NN gibt nur unfug aus. Deswegen hat die Klasse auch eine Funktion mit der das NN auch trainiert werden kann. Es gibt unterschiedliche Mezhoden wie man ein NN trainieren kann. Das "Lernen" was in der Funktion passiert ist auch kein bekannter bzw. oft genutzter Algorithmus. Die Idee liegt darin, dass zu Beginn getestet wird wie gut das NN bereits ist. Anschließend wird eine willkürliche Änderung an dem NN vor genommen. Dadurch ändert sich die Art und Weise, wie das NN auf Input Reagiert. So ändert sich auch das Können des NN. Also wird, nach der Änderung, das NN nochmal getestet. Daraufhin wird verglichen ob die Änderung positive oder negative Auswirkungen auf das Verhalten des NN genommen hat. Sollte es sich gebessert werden, so wird die Änderung gespeichert.
Der Training Befehl tautet:
'''
.train(kurs, type=None)
'''
>type: (Neuron/Layer) Trainingsmodus.
>kurs: Datensatzt an dem trainiert weren soll.