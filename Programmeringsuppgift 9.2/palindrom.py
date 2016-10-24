# -*- coding: latin-1 -*-

#From book 'C fr�n b�rjan'Programmeringsuppgift 9.2, Sida 214
#Skapa ett program som testar om en textstr�ng �r en palindrom
#En palindrom �r en mening som blir samma b�de bakifr�n och
#framifr�n.
#Tips: Ta bort vita tecken och byt ut alla bokst�ver till gemener.

#Exempel:
#Ah Satan sees Natasha
#Dogma I am God
#Flee to me remote elf

text = input("Ange en text f�r att testa palindrom: ")
#sets text_rev to the text reversed, lowercase and removed space characters
text_rev = text[::-1].replace(" ","").lower()  # .replace(x,y) - replaces x with y in string

# triggers if text_rev is same as original text in lowercase, with removed space characters
if (text_rev == text.replace(" ","").lower()): 
	print("Texten \"%s\" �r en palindrom!" % (text)) # \" prints out the character "

else:
	print("Texten \"%s\"�r inte en palindrom!" % (text))