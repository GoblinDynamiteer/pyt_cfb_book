# -*- coding: latin-1 -*-

#From book 'C från början'
#Programmeringsuppgift 9.1, Sida 214
#Skriv en funktion kallad 'baklanges', som kopierar en text
#från ett fält till ett annat, gör kopieringen baklänges!

#function that takes a string, and returns it in reverse
def baklanges(string1): #definition of functions in python
	return string1[::-1] # -1 in slicing means reverse

kalle = "Baklänges"
kalle2 = baklanges(kalle) #sets varible to return value from function baklanges

#prints variables
print(kalle)
print(kalle2)

