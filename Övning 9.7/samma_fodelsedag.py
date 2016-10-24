# -*- coding: latin-1 -*-

#From book 'C fr�n b�rjan'
#�vning 9.7, Sida 206
#Mata in tv� personnummer, fyller personerna �r p� samma dag?
#Anv�nd strncmp(x,y,n):
#J�mf�r x med y, h�gtst n antal tecken
#returnerar 0 om str�ngarna �r lika

pnum1 = input("Ange personnummer 1: ")
pnum2 = input("Ange personnummer 1: ")

#len() returns length of string, if over 11 socialnumber is in 19xx // 20xx format
#var[x:y] is called slicing, returns characters from x to y from string
#var[4:] would return string from fifth/fourth? char to last
if ((len(pnum1) > 11) & (pnum1[2:8] == pnum2[2:8])): #AND is & (not && as in C)
	print("Samma f�delsedag!")
	print(pnum1[2:8])
	
elif((len(pnum1) < 11) & (pnum1[:6] == pnum2[:6])):
	print("Samma f�delsedag!")
	print(pnum1[:6])

else:
	print("Inte samma f�delsedag!")