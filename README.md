# NN-CFDT

## Neural Network for Contract For Difference Traiding

Dieses Programm ist ein Neuronales Netz, welches den zukünftigen Kursverlauf von bestimmten Wertpapieren voraussagen soll.
Es ist in Python geschrieben. Ich habe darauf geachtet möglichst wenige Bibliotheken zu verwenden. Aus dem einfachen Grud, dass dieses Projekt hauptsächlich dazu da ist, dass ich selbst meine Programmier Skills verbessere und NN's, ML und Python besser verstehe.
Ich hoffe man versteht den Code. ;)
Das Projekt ist einbisschen von [tradeucer](http://www.traducer.de/star/include/tabelle.htm) inspiriert...

## How to use it?

am besten ist es die datei `main.py` über die entsprächende Eingabesteuerung des Betriebssytems anzusteuern und auszuführen
damit die Statusanzeigen, Ausgaben bzw. Dialoge sinnvoll genutzt werden können

### Vorarbeit

um das NN zu trainieren braucht es Informationen
dieses NN ist darauf ausgelegt spezielle .csv Dateien mit historischen Kursdaten zu verarbeiten
[Yahoo! Finance](https://finance.yahoo.com/) bietet Historische Daten im perfekten Format für das Programm
lade einfach die Historischen daten des entsprächenden Wertpapiers herunder
anschließend muss die .csv Datei mit in den Ordner `NN-CFDT` gelegt werden

### Programm

1. Starten des Programms `main.py`
2. Eingabe
    - Eingabe der Kursdateien (.csv)
    - Eingabe der Datei in der das NN gespeichert werden soll (.csv)
    - Eingabe der hidden Layer (integer)
    - Eingabe der radikalität des NN (real/float)
3. Verarbeitung der Dateien
    - Verarbeitung der Kursdatei
    - soll das NN zurückgesetzt werden ("True"/"False")
4. Simmulation des NN
    - Ausgabe des Gewinns
5. Lernprozess
    - Eingabe wie lang das NN trainieren soll (integer)
6. Erneute Simulation des NN
    - Ausgabe des Gewinns
7. Live-Voraussage
    - Eingabe des Datums welches ermittelt werden soll (integer)
    - Ausgabe der Voraussage des NN

### Data-Structure

#### Branches
momentan existieren 2 branches
>master

>develop

im master branch wird nur funktionierender Code (ohne Bugs) veröffentlicht
im develop branch können Entwicklungsvortschritte veröffentlicht werden

#### Ordner
alle Dateien liegen in einem Ordner 
>NN-CFDT/

#### Code-Dateien
alle grundlegenden Funktionen liegen in einer Datei
>funktions.py

## How it works

gennerell versuche ich den Code möglichst verständlich zu kommentieren ;)
also empfehle ich auch den Code am Code zu verstehen
die grobe Idee beschreibe ich trotsdem im folgenden

alle wichitgen Funktionen sind in der Datei `funktions.py` nieder geschrieben

### randomizeNN

diese Funktion setzt ein NN zurück
dabei werden alle Werte zufällig bestimmt

### sigmoid

diese Funktion ist nicht wirklich eine Sigmoid Funktion, da momentan das gesammte Sytem auf "Trinär" basiert
es gibt also die Zustände 

>+1: steigend

>0: unsicher

>-1: fallent

deshalb gibt diese Funktion nur einen Wert dieser Zustände aus

### readTable

diese Funktion liest .csv Dateinen ein und gibt ein zweidimensionalen Array aus
das ist auch nur von irgendeinem Tutorial vom YouTube...

### transformKurs

das Programm benötigt eindeutige und immer gleiche Syntax der Kurstabelle
diese Funktion macht aus der .csv Datei von [Yahoo! Finance](https://finance.yahoo.com/) ein für das Programm nützliches Array
außerdem berechnet diese Funktion den Ansteig des Kurses
so wird die .csv Datei von einer anderen ersetzt in der nur eine Spalte liegt in  der nur die Steigung des Kurses geschrieben ist
weil es ncht die Zukunft voraussagen kann und die Überschriften gelöscht werden ist das Array auch 2 Zeilen kleiner als die .csv Dadei

### seperateData

diese Funktion liest aus der .csv Datei den entsprächenden Zeitraum aus
und gibt ihn als Array aus
man muss den name der .csv Datei und die Zeit eingeben aus welchem Zeitraum die Daten haben will
wenn man die neusten Daten haben will gibt man 0 ein

### gues

diese Funktion gibt den gewinn einer Voraussage aus
momentan ist das eine

>+1: gewinn (wahre aussage)

>0: kein Gewinn

>-1: verlohren (falsche aussage)

### layermalweights

Diese Funktion berechnet nach der Eingabe zweier zweidimensionaler Arrays die multiplikation der Matritzen...
Matrixmultiplikation

### NNrechner
das ist das NN
