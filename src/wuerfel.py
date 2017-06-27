# -*- coding: utf-8 -*-

import time as t
from wuerfellib import Wuerfeln

while True:
	# Initialisiere Objekt
	wuerfeln = Wuerfeln()

	# Frage Anzahl der Würfe ab
	while True:
		menge = input ("Wie oft soll gewürfelt werden? ")
		if(menge.isnumeric):
			menge = int(menge)
			break
		else:
			print("Bitte gebe eine gültige Zahl ein")

	# Würfele
	wuerfeln.wuerfele(menge)

	# Gebe Statistik aus
	wuerfeln.Statistik.show()

	# Gebe gebrauchte Zeit aus
	print("--")
	print("Dauer in Sekunden für " + str(wuerfeln.Menge) + "x Würfeln: " + str(wuerfeln.Timer.Time))

	# Schreibe Statistik in csv
	statfile = wuerfeln.StatFile
	print("--")
	print("CSV-Datei mit Ergebnissen: " + statfile)

	print("######################################")
	print("######################################")

	# Lösche die Objekte wieder
	del statfile
	del wuerfeln

	# Mache 1 Sekunde Pause
	t.sleep(1)
