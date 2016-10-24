# -*- coding: latin-1 -*-

#From book 'C från början'Programmeringsuppgift 9.2, Sida 214
#Skapa ett program som testar om en textsträng är en palindrom
#En palindrom är en mening som blir samma både bakifrån och
#framifrån.
#Tips: Ta bort vita tecken och byt ut alla bokstäver till gemener.

#Exempel:
#Ah Satan sees Natasha
#Dogma I am God
#Flee to me remote elf

text = input("Ange en text för att testa palindrom: ")
#sets text_rev to the text reversed, lowercase and removed space characters
text_rev = text[::-1].replace(" ","").lower()  # .replace(x,y) - replaces x with y in string

# triggers if text_rev is same as original text in lowercase, with removed space characters
if (text_rev == text.replace(" ","").lower()): 
	print("Texten \"%s\" är en palindrom!" % (text)) # \" prints out the character "

else:
	print("Texten \"%s\"är inte en palindrom!" % (text))