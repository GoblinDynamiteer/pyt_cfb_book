# -*- coding: latin-1 -*-

#From book 'C från början'
#Programmeringsuppgift 8.8, Sida 180
#Skriv ett program som beräkna och lägger de första 50 primtalen i en array. 
#Skriv ut fältet. 
#Ett primtal är ett tal som enbart är jämnt delbart med sig själv (och talet 1).

primes = []
i = 2 #to check if prime number
n = 0 #counter for prime numbers stored in list
while not (n == 50): #loops until n reaches 50 (amounts of prime numbers to store in list)
	notprime = 0
	for x in range(2,(i-1)):
		if(i % x) == 0: #checks if modulus of i (number to check) and x (range from 2 to i-1) is zero
			notprime = 1 #not very good solution..
	if (notprime == 0):
		primes.append(i) #appends number i to list, i is a prime number
		n += 1 #as n++, doesnt seem to work in python?
	i += 1 #i++

for i in range(0, len(primes)):	#prints values in list
	print("Prime number", i+1, ":", primes[i])
