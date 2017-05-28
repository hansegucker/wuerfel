# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel,
    QMessageBox,
    QApplication)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from wuerfellib import Wuerfeln

####################
# Zusatzfunktionen #
####################

# def center(gui):
#     """ Zentriert ein Fenster """
#
#     qr = gui.frameGeometry()
#     cp = QDesktopWidget().availableGeometry().center()
#     qr.moveCenter(cp)
#     gui.move(qr.topLeft())

#############################
# Initialisierungen Fenster #
#############################

# def initwuerfelgui():
#     """ Initialisiert die GUI der Startansicht"""
#
#     global wuerfelgui
#
#     startlabel = QLabel("Anzahl der Würfelvorgänge: ")
#     wuerfelgui.starttextbox = QLineEdit("1000")
#     copyrightlabel = QLabel("(C) 2017 by Jonathan Weth (joniweth@gmx.de)")
#
#     startbutton = QPushButton("Würfeln")
#     startbutton.setToolTip("Klicke auf diesen Button, um den <b>Würfelvorgang</b> zu starten")
#     startbutton.clicked.connect(startwuerfeln)
#
#     # Horizontal (--)
#     hbox = QHBoxLayout()
#     hbox.addWidget(startlabel)
#     hbox.addWidget(wuerfelgui.starttextbox)
#
#     # Vertikal (I)
#     vbox = QVBoxLayout()
#     vbox.addLayout(hbox)
#     vbox.addWidget(startbutton)
#     vbox.addWidget(copyrightlabel)
#
#     wuerfelgui.setLayout(vbox)
#
#     # Größe und Position
#     #wuerfelgui.setGeometry(300, 100, 300, 10)
#     center(wuerfelgui)
#
#     # Aussehen
#     wuerfelgui.setWindowTitle('Würfel')
#     wuerfelgui.setWindowIcon(QIcon('wuerfelicon-small.png'))
#
#     # Fenster zeigen
#     wuerfelgui.show()

# def initergebnisgui(wuerfeln):
#     """ Initialisiert die Ergebnisansicht """
#
#     global ergebnisgui
#     # Größe und Position
#     #ergebnisgui.setGeometry(300, 300, 300, 220)
#     center(ergebnisgui)
#
#     # Aussehen
#     ergebnisgui.setWindowTitle('Ergebnis - Würfel')
#     ergebnisgui.setWindowIcon(QIcon('wuerfelicon-small.png'))

    # copyrightlabel = QLabel("(C) 2017 by Jonathan Weth (joniweth@gmx.de)")
    #
    # ergebnislabel = QLabel("<h1>ERGEBNIS</h1>")
    # ergebnislabel.setAlignment(Qt.AlignCenter)
    # anzahllabel = QLabel("Anzahl der Würfe: ")
    # anzahlvaluelabel = QLabel(str(wuerfeln.Menge))
    # timelabel = QLabel("Dauer (in Sekunden): ")
    # timevaluelabel = QLabel(str(wuerfeln.Timer.Time))

    # anzahlhbox = QHBoxLayout()
    # anzahlhbox.addWidget(anzahllabel)
    # anzahlhbox.addWidget(anzahlvaluelabel)
    # timehbox = QHBoxLayout()
    # timehbox.addWidget(timelabel)
    # timehbox.addWidget(timevaluelabel)

    # statboxes = {}
    # statlabels = {}
    # statvaluelabels = {}
    #
    # for key in wuerfeln.Statistik.Statistik.keys():
    #     statlabels[key] = QLabel(key + "er: ")
    #     statvaluelabels[key] = QLabel(str(wuerfeln.Statistik.Statistik[key]))
    #     statboxes[key] = QHBoxLayout()
    #     statboxes[key].addWidget(statlabels[key])
    #     statboxes[key].addWidget(statvaluelabels[key])

    # # Vertikal (I)
    # vbox = QVBoxLayout()
    # vbox.addWidget(ergebnislabel)
    # vbox.addLayout(anzahlhbox)
    # for key in wuerfeln.Statistik.Statistik.keys():
    #     vbox.addLayout(statboxes[key])
    # vbox.addLayout(timehbox)
    # vbox.addWidget(copyrightlabel)
    #
    # ergebnisgui.setLayout(vbox)
    #
    # # Fenster zeigen
    # ergebnisgui.show()

def initwaitgui():
    """ Initialisiert die Warteansicht """
    #
    # global waitgui
    # # Größe und Position
    # #waitgui.setGeometry(300, 300, 300, 220)
    # center(waitgui)
    #
    # # Aussehen
    # waitgui.setWindowTitle('Bitte warten ...')
    # waitgui.setWindowIcon(QIcon('wuerfelicon-small.png'))

    # # Bitte warten
    # waitlabel = QLabel("Bitte warten ...")
    #
    # hbox = QHBoxLayout()
    # hbox.addWidget(waitlabel)
    #
    # waitgui.setLayout(hbox)
    #
    # # Fenster zeigen
    # waitgui.show()

###################
# Eventfunktionen #
###################

def startwuerfeln():
    """ Startet den Würfelvorgang """
    #
    # global wuerfelgui
    # print("Starte Würfelvorgang ...")
    # menge = wuerfelgui.starttextbox.text()
    # if(menge.isnumeric()):
    #     menge = int(menge)
    #     print("Anzahl ist numerisch!")
    #     print("Anzahl: " + str(wuerfelgui.starttextbox.text()))
    #
    #     # Öffne Ergebnisansicht und schließe Startansicht
    #     initwaitgui()
    #     wuerfelgui.hide()

        # Würfele
        wuerfeln = Wuerfeln()
        wuerfeln.wuerfele(menge)
        initergebnisgui(wuerfeln)
        waitgui.hide()
    # else:
    #     QMessageBox.warning(wuerfelgui, 'Fehler',
    #         "Bitte geben sie eine gültige Zahl ein!")
    #     wuerfelgui.setFocus()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    wuerfelgui = QWidget()
    ergebnisgui = QWidget()
    waitgui = QWidget()

    # Zeige Fenster
    initwuerfelgui()
    sys.exit(app.exec_())
