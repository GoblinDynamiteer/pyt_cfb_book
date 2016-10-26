# -*- coding: latin-1 -*-
from sys import stdin

#From book 'C från början'
#Övning 14.2, Sida 348
#Lägg till i modulen 'array_list': en funktion 'remove_last', som tar bort det sista elementet. 
#Funktionen ska returnera en pekare till det borttagna elementet om det gick bra, annars NULL. 

list = []; #creates empty list
print("Skriv in heltal: ")
for line in stdin:
	print("Skriv in heltal (avsluta med ctrl+z): ")
	list.append(int(line)) #float(x) converts string x to float
	
print("Antal element i listan:", len(list)) #len(x) gets number of elements in list x

for i in range(len(list)): #range(x) returns a list of integers from 0 to x
	print("Sista värdet i listan:", list[len(list)-1])  #list[x] returns element x in list
	print("Tog bort sista värdet i listan: ", list.pop()) # list.pop() removes and returns the last element in list


