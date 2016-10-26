# -*- coding: latin-1 -*-
from sys import stdin

#From book 'C från början'
#Övning 14.1, Sida 346
#Skriv ett program som läser in ett godtyckligt antal tal. 
#Avsluta inläsning med EOF. 
#Programmet ska lägga de inlästa talen i en lista. 
#När inläsningen avslutats ska programmet löpa igenom listan och undersöka vilket av talen som är störst. 
#Detta tal och dess index ska skrivas ut. 

#Använd list.h och list.c från bokens hemsida.

list = []; #creates empty list
print("Skriv in värde: ")
for line in stdin:
	print("Skriv in värde (avsluta med ctrl+z): ")
	list.append(float(line)) #float(x) converts string x to float

print("Antal element i listan:", len(list)) #len(x) gets number of elements in list x
#max(x) returns the max value of elements in list
#list.index(x) returns index of value x in list 'list' (first occurrence)
print("Max:", max(list), "på index", list.index(max(list)))	

