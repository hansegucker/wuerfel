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

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.Labels = {}
        self.Buttons = {}
        self.Edits = {}
        self.Layouts = {}
        self.Labels["copyright"] = QLabel("(C) 2017 by Jonathan Weth (joniweth@gmx.de)")

    def center(self):
        """ Zentriert das Fenster """

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class StartUI(Window):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Widgets
        self.Labels["anzahl"] = QLabel("Anzahl der Würfelvorgänge")
        self.Edits["anzahl"] = QLineEdit("1000")

        self.Buttons["start"] = QPushButton("Würfeln")
        self.Buttons["start"].setToolTip("Klicke auf diesen Button, um den <b>Würfelvorgang</b> zu starten")
        self.Buttons["start"].clicked.connect(self.start)

        # Layouts
        self.Layouts["hbox1"] = QHBoxLayout()
        self.Layouts["hbox1"].addWidget(self.Labels["start"])
        self.Layouts["hbox1"].addWidget(self.Edits["start"])

        self.Layouts["vbox"] = QVBoxLayout()
        self.Layouts["vbox"].addLayout(self.Layouts["hbox1"])
        self.Layouts["vbox"].addWidget(self.Buttons["start"])
        self.Layouts["vbox"].addWidget(self.Labels["copyright"])

        self.setLayout(self.Layouts["vbox"])

        # Aussehen und Position
        self.center()

        self.setWindowTitle("Würfel")
        self.setWindowIcon(QIcon("wuerfelicon-small.png"))

        # Zeigen
        self.show()

    def start(self):
        pass

class ErgebnisUI(Window):
    def __init__(self, wuerfeln):
        super().__init__()
        self.Wuerfeln = wuerfeln
        self.initUI()

    def initUI(self):
        # Widgets
        self.Labels["title"] = QLabel("<h1>ERGEBNIS</h1>")
        self.Labels["title"].setAlignment(Qt.AlignCenter)

        self.Labels["anzahl"] = QLabel("Anzahl der Würfe: ")
        self.Labels["anzahlvalue"] = QLabel(str(self.Wuerfeln.Menge))

        self.Labels["time"] = QLabel("Dauer (in Sekunden): ")
        self.Labels["timevalue"] = QLabel(str(self.Wuerfeln.Timer.Time))

        # Layouts für Widgets (anzahl, time)
        self.Layouts["anzahlhbox"] = QHBoxLayout()
        self.Layouts["anzahlhbox"].addWidget(self.Labels["anzahl"])
        self.Layouts["anzahlhbox"].addWidget(self.Labels["anzahlvalue"])

        self.Layouts["timehbox"] = QHBoxLayout()
        self.Layouts["timehbox"].addWidget(self.Labels["time"])
        self.Layouts["timehbox"].addWidget(self.Labels["timevalue"])

        # Layout und Widgets für Würfelergebnisse
        self.Layouts["stat"] = {}
        self.Labels["stat"] = {}
        self.Labels["statvalue"] = {}

        # Alle Würfel durchgehen
        keys = self.Wuerfeln.Statistik.Statistik.keys()
        for key in keys:
            self.Labels["stat"][key] = QLabel(key + "er: ")
            self.Labels["statvalue"][key] = QLabel(str(keys[key]))
            self.Layouts["stat"][key] = QHBoxLayout()
            self.Layouts["stat"][key].addWidget(self.Labels["stat"][key])
            self.Layouts["stat"][key].addWidget(self.Labels["statvalue"][key])

        # Layouts
        self.Layouts["vbox"] = QVBoxLayout()

        self.Layouts["vbox"].addWidget(self.Labels["title"])
        self.Layouts["vbox"].addLayout(self.Layouts["anzahl"])

        for key in keys:
            self.Layouts["vbox"].addLayout(self.Layouts["stat"][key])

        self.Layouts["vbox"].addLayout(self.Layouts["time"])
        self.Layouts["vbox"].addWidget(self.Labels["copyright"])

        self.setLayout(self.Layouts["vbox"])

        self.show()
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
#
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
#
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
#
#     copyrightlabel = QLabel("(C) 2017 by Jonathan Weth (joniweth@gmx.de)")
#
#     ergebnislabel = QLabel("<h1>ERGEBNIS</h1>")
#     ergebnislabel.setAlignment(Qt.AlignCenter)
#     anzahllabel = QLabel("Anzahl der Würfe: ")
#     anzahlvaluelabel = QLabel(str(wuerfeln.Menge))
#     timelabel = QLabel("Dauer (in Sekunden): ")
#     timevaluelabel = QLabel(str(wuerfeln.Timer.Time))
#
#     anzahlhbox = QHBoxLayout()
#     anzahlhbox.addWidget(anzahllabel)
#     anzahlhbox.addWidget(anzahlvaluelabel)
#     timehbox = QHBoxLayout()
#     timehbox.addWidget(timelabel)
#     timehbox.addWidget(timevaluelabel)
#
#     statboxes = {}
#     statlabels = {}
#     statvaluelabels = {}
#
#     for key in wuerfeln.Statistik.Statistik.keys():
#         statlabels[key] = QLabel(key + "er: ")
#         statvaluelabels[key] = QLabel(str(wuerfeln.Statistik.Statistik[key]))
#         statboxes[key] = QHBoxLayout()
#         statboxes[key].addWidget(statlabels[key])
#         statboxes[key].addWidget(statvaluelabels[key])
#
#     # Vertikal (I)
#     vbox = QVBoxLayout()
#     vbox.addWidget(ergebnislabel)
#     vbox.addLayout(anzahlhbox)
#     for key in wuerfeln.Statistik.Statistik.keys():
#         vbox.addLayout(statboxes[key])
#     vbox.addLayout(timehbox)
#     vbox.addWidget(copyrightlabel)
#
#     ergebnisgui.setLayout(vbox)
#
#     # Fenster zeigen
#     ergebnisgui.show()
#
# def initwaitgui():
#     """ Initialisiert die Warteansicht """
#
#     global waitgui
#     # Größe und Position
#     #waitgui.setGeometry(300, 300, 300, 220)
#     center(waitgui)
#
#     # Aussehen
#     waitgui.setWindowTitle('Bitte warten ...')
#     waitgui.setWindowIcon(QIcon('wuerfelicon-small.png'))
#
#     # Bitte warten
#     waitlabel = QLabel("Bitte warten ...")
#
#     hbox = QHBoxLayout()
#     hbox.addWidget(waitlabel)
#
#     waitgui.setLayout(hbox)
#
#     # Fenster zeigen
#     waitgui.show()
#
# ###################
# # Eventfunktionen #
# ###################
#
# def startwuerfeln():
#     """ Startet den Würfelvorgang """
#
#     global wuerfelgui
#     print("Starte Würfelvorgang ...")
#     menge = wuerfelgui.starttextbox.text()
#     if(menge.isnumeric()):
#         menge = int(menge)
#         print("Anzahl ist numerisch!")
#         print("Anzahl: " + str(wuerfelgui.starttextbox.text()))
#
#         # Öffne Ergebnisansicht und schließe Startansicht
#         initwaitgui()
#         wuerfelgui.hide()
#
#         # Würfele
#         wuerfeln = Wuerfeln()
#         wuerfeln.wuerfele(menge)
#         initergebnisgui(wuerfeln)
#         waitgui.hide()
#     else:
#         QMessageBox.warning(wuerfelgui, 'Fehler',
#             "Bitte geben sie eine gültige Zahl ein!")
#         wuerfelgui.setFocus()
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     wuerfelgui = QWidget()
#     ergebnisgui = QWidget()
#     waitgui = QWidget()
#
#     # Zeige Fenster
#     initwuerfelgui()
#     sys.exit(app.exec_())
