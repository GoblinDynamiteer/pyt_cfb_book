# -*- coding: latin-1 -*-
from sys import stdin

#From book 'C fr�n b�rjan'
#�vning 14.1, Sida 346
#Skriv ett program som l�ser in ett godtyckligt antal tal. 
#Avsluta inl�sning med EOF. 
#Programmet ska l�gga de inl�sta talen i en lista. 
#N�r inl�sningen avslutats ska programmet l�pa igenom listan och unders�ka vilket av talen som �r st�rst. 
#Detta tal och dess index ska skrivas ut. 

#Anv�nd list.h och list.c fr�n bokens hemsida.

list = []; #creates empty list
print("Skriv in v�rde: ")
for line in stdin:
	print("Skriv in v�rde (avsluta med ctrl+z): ")
	list.append(float(line)) #float(x) converts string x to float

print("Antal element i listan:", len(list)) #len(x) gets number of elements in list x
#max(x) returns the max value of elements in list
#list.index(x) returns index of value x in list 'list' (first occurrence)
print("Max:", max(list), "p� index", list.index(max(list)))	

