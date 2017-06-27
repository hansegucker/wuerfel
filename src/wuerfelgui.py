# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel,
    QMessageBox,
    QApplication)
from PyQt5.QtGui import QIcon, QFont, QPixmap
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
        self.Layouts["hbox1"].addWidget(self.Labels["anzahl"])
        self.Layouts["hbox1"].addWidget(self.Edits["anzahl"])

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
        menge = self.Edits["anzahl"].text()
        if(menge.isnumeric()):
            menge = int(menge)
            print("Anzahl ist numerisch!")
            print("Anzahl: " + str(menge))

            # Öffne Warteansichtund schließe Startansicht
            self.hide()
            self.WaitUI = WaitUI(menge)
        else:
            QMessageBox.warning(self, 'Fehler',
                "Bitte geben sie eine gültige Zahl ein!")
            self.setFocus()

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
        for key in self.Wuerfeln.Statistik.Statistik.keys():
            self.Labels["stat"][key] = QLabel(key + "er: ")
            self.Labels["statvalue"][key] = QLabel(str(self.Wuerfeln.Statistik.Statistik[key]))
            self.Layouts["stat"][key] = QHBoxLayout()
            self.Layouts["stat"][key].addWidget(self.Labels["stat"][key])
            self.Layouts["stat"][key].addWidget(self.Labels["statvalue"][key])

        # Layouts
        self.Layouts["vbox"] = QVBoxLayout()

        self.Layouts["vbox"].addWidget(self.Labels["title"])
        self.Layouts["vbox"].addLayout(self.Layouts["anzahlhbox"])

        for key in self.Wuerfeln.Statistik.Statistik.keys():
            self.Layouts["vbox"].addLayout(self.Layouts["stat"][key])

        self.Layouts["vbox"].addLayout(self.Layouts["timehbox"])
        self.Layouts["vbox"].addWidget(self.Labels["copyright"])

        self.setLayout(self.Layouts["vbox"])

        # Aussehen und Position
        self.center()

        self.setWindowTitle("Ergebnis - Würfel")
        self.setWindowIcon(QIcon('wuerfelicon-small.png'))

        # Zeigen
        self.show()

class WaitUI(Window):
    def __init__(self, menge):
        super().__init__()
        self.Menge = menge
        self.initUI()
        self.do()

    def do(self):
        wuerfeln = Wuerfeln()
        wuerfeln.wuerfele(self.Menge)
        self.hide()
        self.ErgebnisUI = ErgebnisUI(wuerfeln)

    def initUI(self):
        # Widgets
        pixmap = QPixmap("waiticon-small.png")
        self.Labels["wait"] = QLabel("Bitte warten ...")
        self.Labels["icon"] = QLabel()
        self.Labels["icon"].setPixmap(pixmap)

        # Layouts
        self.Layouts["hbox"] = QHBoxLayout()
        self.Layouts["hbox"].addWidget(self.Labels["wait"])
        self.Layouts["hbox"].addWidget(self.Labels["icon"])

        self.setLayout(self.Layouts["hbox"])

        # Aussehen und Position
        self.center()

        self.setWindowTitle('Bitte warten ...')
        self.setWindowIcon(QIcon('wuerfelicon-small.png'))

        # Zeigen
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = StartUI()

    sys.exit(app.exec_())
