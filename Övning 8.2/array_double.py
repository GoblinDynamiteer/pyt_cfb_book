# -*- coding: latin-1 -*-

#From book 'C från början'
#Övning 8.2, Sida 155
#Skapa ett fält med tio element, typ double.
#Använd en for-sats för att ge fälten värdet 1/1, 1/2, 1/3 osv
#Sist ska värdena skrivas ut!

#Lists are similar to arrays in C, but can hold any value (kinda like a struct)
list = [] #creates empty list

#for-loop for 1-10 (dont know why has to be eleven, maybe UP TO 11)
for num in range(1,11): #Indenting is used to encapsulate, instead of curly brackets
	list.append(1 / num); #appends valdue of 1/num to list

#prints the values in the list, with index
for num in range(0,10):
	print ("list[%d] = %.3f" % (num, list[num]))
	#print("Blah %d Bleh % (IntVar)	)
	#Similar format output as C, %d - %.4f etc
