import random as rd
import time as t
def wuerfele():
	return rd.randint(1,6)
statistik = [0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
	menge = input ("Wie oft soll gewürfelt werden?")
	menge = int(menge)
	starttime = t.time()
	for i in range(menge):
		a = wuerfele()
		b = wuerfele()
		c = a + b
		#print ("Würfel 1: "+str(a))
		#print ("Würfel 2: "+str(b))
		#print ("Würfelaugensumme: "+str(c))
		#print ("-----")
		statistik[c] = statistik[c] + 1
	endtime = t.time()
	print ("###########")
	print ("#Statistik#")
	print ("###########")
	for i in range(len(statistik)):
		print(str(i)+"er: "+str(statistik[i]))
	print()
	time = endtime - starttime
	print("Dauer in Sekunden für "+str(menge)+"x Würfeln: "+str(time))
