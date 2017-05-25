
import time as t


class Wuerfel(object):
	import random as rd

	def __init__(self):
		pass

	def wuerfele():
		return self.rd.randinit(1,6)

class Statistik(object):
	import csv as csv
	Statistik = {}

	def __init__(self, keys = "123456", keytitle = "Wert", valuetitle = "Anzahl"]):
		# Initialisiere Statistik-Array
		for key in keys:
			self.Statistik[key] = 0
		# Titel festlegen
		self.KeyTitle = keytitle
		self.ValueTitle = valuetitle

	def writecsv(self, filename, extrainfos={"Test": "Test"}):
		with open(filename, 'wt') as csvfile:
			csvwriter = csv.writer(csvfile)
			# Titelzeile schreiben
			csvwriter.writerow([self.KeyTitle, self.ValueTitle])
			# Schreibe Statistik
			for key in self.Statistik.keys():
  				csvwriter.writerow([key, str(self.Statistik[key])])
			# Schreibe Zusatzinfo
			for key in extrainfos.keys():
				csvwriter.writerow([key, extrainfos[key]])

	def add(self, key):
		self.Statistik[key] = self.Statistik[key] + 1

class Timer(object):
	import time as t
	Time = 0
	StartTime = 0
	EndTime = 0

	def __init__(self):
		pass

	def start(self):
		if(self.Running == False):
			self.StartTime = t.time()
			self.Running = True
			self.Time = 0
		else:
			print("Bitte stoppe zuerst den Timer!")

	def stop(self):
		if(self.Running):
			self.EndTime = t.time()
			self.Running = False
			self.Time = self.EndTime - self.StartTime
		else:
			print("Bitte starte zuerst den Timer.")

	def get(self):
		return self.Time
		
while True:
	try:
		statistik = Statistik("123456", "Augenzahl", "Anzahl")
		menge = input ("Wie oft soll gewürfelt werden? ")
		menge = int(menge)
		starttime = t.time()

		# Würfeln
		for i in range(menge):
			a = wuerfele()
			# b = wuerfele()
			c = a # + b
			#print ("Würfel 1: "+str(a))
			#print ("Würfel 2: "+str(b))
			#print ("Würfelaugensumme: "+str(c))
			#print ("-----")
			statistik[c] = statistik[c] + 1

		# Gebe Statistik aus
		endtime = t.time()
		print ("#############")
		print ("# Statistik #")
		print ("#############")
		# Würfel 0-12
		for i in range(len(statistik)):
			print(str(i) + "er: " + str(statistik[i]))
		print()
		time = endtime - starttime
		print("Dauer in Sekunden für " + str(menge) + "x Würfeln: " + str(time))

		# Schreibe Statistik in csv
		statfile = "wuerfeln" + str(endtime) + ".csv"
		writestat(statistik, statfile, menge)
		print("#############")
		print("Ergebnisse in csv: " + statfile)
	except:
		print("FEHLER!")
		exit()

	t.sleep(1)
