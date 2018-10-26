# NN-CFDT

## Neural Network for Contract For Difference Traiding

## How to use it?

am besten ist es die datei ´main.py´ über die entsprächende Eingabesteuerung des Betriebssytems anzusteuern und auszuführen
damit die Statusanzeigen, Ausgaben bzw. Dialoge sinnvoll genutzt werden können

1. Starten des Programms ´main.py´
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

momentan existieren 2 branches
>master

>develop
im master branch wird nur funktionierender Code (ohne Bugs) veröffentlicht
im develop branch können Entwicklungsvortschritte veröffentlicht werden

alle Dateien liegen in einem Ordner 
>NN-CFDT/

alle grundlegenden Funktionen liegen in einer Datei
>funktions.py

folgende Dateien enthalten meist code, der die Funktionen in funktions.py nützlich machen (mit Ausgabe)
>dauertestNN.py

>NN-CFDT.py

>randomizeNN.py

>trainNNday.py

>trainNNyear.py

>transformNN.py