import random as rd
import time as t
import csv as csv
# import matplotlib.pyplot as pyplot
# import pandas as pandas

# INIT
def wuerfele():
	return rd.randint(1,6)

def writestat(stat, filename, summe):
	with open(filename, 'wt') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(['Würfel', 'Anzahl'])
		for i in range(len(stat)):
			csvwriter.writerow([str(i) + "er: ", str(stat[i])])
		csvwriter.writerow(["Summe", summe])
		


while True:
	try:
		statistik = [0,0,0,0,0,0,0]
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
