# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel,
    QMessageBox,
    QApplication)
from PyQt5.QtGui import QIcon, QFont

####################
# Zusatzfunktionen #
####################

def center(gui):
    """ Zentriert ein Fenster """

    qr = gui.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    gui.move(qr.topLeft())

#############################
# Initialisierungen Fenster #
#############################

def initwuerfelgui():
    """ Initialisiert die GUI der Startansicht"""

    global wuerfelgui

    startlabel = QLabel("Anzahl der Würfelvorgänge: ")
    wuerfelgui.starttextbox = QLineEdit("1000")

    startbutton = QPushButton("Würfeln")
    startbutton.setToolTip("Klicke auf diesen Button, um den <b>Würfelvorgang</b> zu starten")
    startbutton.clicked.connect(startwuerfeln)

    # Horizontal (--)
    hbox = QHBoxLayout()
    hbox.addWidget(startlabel)
    hbox.addWidget(wuerfelgui.starttextbox)

    # Vertikal (I)
    vbox = QVBoxLayout()
    vbox.addLayout(hbox)
    vbox.addWidget(startbutton)

    wuerfelgui.setLayout(vbox)

    # Größe und Position
    wuerfelgui.setGeometry(300, 300, 300, 220)
    center(wuerfelgui)

    # Aussehen
    wuerfelgui.setWindowTitle('Würfel')
    wuerfelgui.setWindowIcon(QIcon('wuerfelicon-small.png'))

    # Fenster zeigen
    wuerfelgui.show()

def initergebnisgui():
    """ Initialisiert die Ergebnisansicht """

    global ergebnisgui
    # Größe und Position
    ergebnisgui.setGeometry(300, 300, 300, 220)
    center(ergebnisgui)

    # Aussehen
    ergebnisgui.setWindowTitle('Ergebnis - Würfel')
    ergebnisgui.setWindowIcon(QIcon('wuerfelicon-small.png'))

    # Fenster zeigen
    ergebnisgui.show()

def initwaitgui():
    """ Initialisiert die Warteansicht """

    global waitgui
    # Größe und Position
    waitgui.setGeometry(300, 300, 300, 220)
    center(waitgui)

    # Aussehen
    waitgui.setWindowTitle('Bitte warten ...')
    waitgui.setWindowIcon(QIcon('wuerfelicon-small.png'))

    # Bitte warten
    waitlabel = QLabel("Bitte warten ...")

    hbox = QHBoxLayout()
    hbox.addWidget(waitlabel)

    waitgui.setLayout(hbox)

    # Fenster zeigen
    waitgui.show()

##################
# Resets Fenster #
##################

def resetwuerfelgui():
    """ Setzt die Startansicht zurück """

    global wuerfelgui
    wuerfelgui.starttextbox.clear()
    wuerfelgui.starttextbox.insert("1000")

###################
# Eventfunktionen #
###################

def startwuerfeln():
    """ Startet den Würfelvorgang """

    global wuerfelgui
    print("Starte Würfelvorgang ...")
    menge = wuerfelgui.starttextbox.text()
    if(menge.isnumeric()):
        menge = int(menge)
        print("Anzahl ist numerisch!")
        print("Anzahl: " + str(wuerfelgui.starttextbox.text()))

        # Öffne Ergebnisansicht und schließe Startansicht
        initwaitgui()
        wuerfelgui.hide()
    else:
        QMessageBox.warning(wuerfelgui, 'Fehler',
            "Bitte geben sie eine gültige Zahl ein!")
        wuerfelgui.setFocus()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    wuerfelgui = QWidget()
    ergebnisgui = QWidget()
    waitgui = QWidget()

    # Zeige Fenster
    initwuerfelgui()
    sys.exit(app.exec_())
