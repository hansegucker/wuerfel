# -*- coding: utf-8 -*-

class Wuerfel(object):
	import random as rd

	def __init__(self):
		pass

	def wuerfele(self):
		""" Würfelt eine Zahl zwischen 1 und 6

		Argumente: 	keine
		Rückgabe: 	gewürfelte Zahl
		"""

		return self.rd.randint(1,6)

class Statistik(object):
	import csv as csv
	Statistik = {}

	def __init__(self, keys = "123456", keytitle = "Wert", valuetitle = "Anzahl"):
		""" Initialisiert ein neues Statistikobjekt

		Argumente:	keys > Array oder String > Schlüsselwörter für die statistischen Objekte > Standard: 123456
					keytitle > String > Titel für die Schlüsselwörter > Standard: Wert
					valuetitle > String > Titel für die erfassten Werte > Standard: Anzahl
		Rückgabe: 	keine
		"""

		# Initialisiere Statistik-Array
		for key in keys:
			self.Statistik[key] = 0
		# Titel festlegen
		self.KeyTitle = keytitle
		self.ValueTitle = valuetitle

	def writecsv(self, filename = "ergebnisse.csv", extrainfos = {"": ""}):
		""" Schreibt die Statistik in eine CSV-Datei

		Argumente: 	filename > String > Name der CSV-Datei
					extrainfos > Dictionary > zusätzliche Infos, die auch in die CSV-Datei geschrieben werden
		Rückgabe: 	keine
		"""

		with open(filename, 'wt') as csvfile:
			csvwriter = self.csv.writer(csvfile)
			# Titelzeile schreiben
			csvwriter.writerow([self.KeyTitle, self.ValueTitle])
			# Schreibe Statistik
			for key in self.Statistik.keys():
  				csvwriter.writerow([key, str(self.Statistik[key])])
			# Schreibe Zusatzinfo
			for key in extrainfos.keys():
				csvwriter.writerow([key, extrainfos[key]])

	def show(self):
		""" Zeigt die Statistik im CLI

		Argumente:	keine
		Rückgabe:	keine
		"""

		print("#############")
		print("# Statistik #")
		print("#############")
		for key in self.Statistik.keys():
			print(key + ": " + str(self.Statistik[key]))

	def add(self, key):
		self.Statistik[key] = self.Statistik[key] + 1

class Timer(object):
	import time as t
	Time = 0 # gemessene Zeit
	StartTime = 0 # Start der Messung
	EndTime = 0 # Ende der Messung
	Running = False # Läuft die Messung?

	def __init__(self):
		pass

	def start(self):
		""" Startet den Timer

		Argumente: 	keine
		Rückgabe: 	keine
		"""

		if(self.Running == False):
			self.StartTime = self.t.time()
			self.Running = True
			self.Time = 0
		else:
			print("Bitte stoppe zuerst den Timer!")

	def stop(self):
		""" Stoppt den Timer

		Argumente: 	keine
		Rückgabe: 	keine
		"""

		if(self.Running):
			self.EndTime = self.t.time()
			self.Running = False
			self.Time = self.EndTime - self.StartTime
		else:
			print("Bitte starte zuerst den Timer.")

	def get(self):
		""" Übergibt die gemessene Zeit

		Argumente:	keine
		Rückgabe: 	gemessene Zeit
		"""

		return self.Time

class Wuerfeln(object):
	Menge = 0
	StatFile = ""

	def __init__(self):
		# Initialisiere Objekte
		self.Statistik = Statistik("123456", "Augenzahl", "Anzahl")
		self.Wuerfel = Wuerfel()
		self.Timer = Timer()

	def wuerfele(self, menge):
		self.Menge = menge

		# Starte den Timer
		self.Timer.start()

		# Würfeln
		for i in range(self.Menge):
			x = self.Wuerfel.wuerfele()
			self.Statistik.add(str(x))

		# Stoppe Timer
		self.Timer.stop()

		# Schreibe Statistik in csv
		try:
			self.StatFile = "wuerfeln" + str(self.Timer.Time) + ".csv"
			self.Statistik.writecsv(self.StatFile, {"Anzahl der Würfe: ": menge})
		except:
			print("Leider konnte die CSV-Datei nicht geschrieben werden!")
