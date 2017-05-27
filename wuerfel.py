# -*- coding: utf-8 -*-

import time as t
from wuerfellib import Wuerfel, Timer, Statistik


while True:
	# Initialisiere Objekte
	statistik = Statistik("123456", "Augenzahl", "Anzahl")
	wuerfel = Wuerfel()
	timer = Timer()

	# Frage Anzahl der Würfe ab
	while True:
		menge = input ("Wie oft soll gewürfelt werden? ")
		if(menge.isnumeric):
			menge = int(menge)
			break
		else:
			print("Bitte gebe eine gültige Zahl ein")

	# Starte den Timer
	timer.start()

	# Würfeln
	for i in range(menge):
		x = wuerfel.wuerfele()
		statistik.add(str(x))

	# Stoppe Timer
	timer.stop()

	# Gebe Statistik aus
	statistik.show()

	# Gebe gebrauchte Zeit aus
	print("--")
	print("Dauer in Sekunden für " + str(menge) + "x Würfeln: " + str(timer.Time))

	# Schreibe Statistik in csv
	try:
		statfile = "wuerfeln" + str(timer.Time) + ".csv"
		print("--")
		print("CSV-Datei mit Ergebnissen: " + statfile)
		statistik.writecsv(statfile, {"Anzahl der Würfe: ": menge})
	except:
		print("Leider konnte die CSV-Datei nicht geschrieben werden!")

	print("######################################")
	print("######################################")

	# Lösche die Objekte wieder
	del menge, statfile
	del wuerfel
	del statistik
	del timer

	# Mache 1 Sekunde Pause
	t.sleep(1)
