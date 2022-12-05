#Funkcja ord()

# print(ord("A"))
# print(ord("Z"))
# # w python kody ASCII wielkich liter A-Z są od 65 do 90

# #Fubkcja chr() - zwraca znak dla danego kodu
# print(chr(66))
# print(chr(75))

#zadanie testowe: wypisz alfabet liter wielkich

# for i in range(66,91):
#      print(chr(i), end="")

# String w python - lista
# #len- długość napisu


napis="KOT"
szyfr= ""
print(napis[0], napis[1],  napis[2])
print(len(napis))

 for i in range(len(napis)):
     print(napis[i])
    szyfr= szyfr+ chr(65 +((ord(napis[i]-65)+3) % 26))
print(szyfr)      
