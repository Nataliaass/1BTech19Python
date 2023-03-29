# #wczytaj dowolny napis i wypisz z niego pierwsza i ostatnia literke
# s=input()
# print(s[0], s[-1])
# # 2.wczytaj dowolny napis i wypisz z niego literki bez pierwszej bez ostatniej
# a=input()
# for i in range(1, len(a)-1):
#   print(a[i], end-"")
# print()
# #lub
# print(a[1:len(a)-1])
# #3. Wypisz 4 ostanie literki z wpisanego napisu w kolejnosci od konca
# b= input()
# for i in range(len(b)-1), len(b)-5, -1):
#   print(b[i], end="")
# print()
# #2:
# L=list(b)
# L.reverse()
# b= " ".join(L)
# for i in range(4):
#   print(L[i], end="")
# print()
# #3:
# print(b[len(b)-1: len(b)-5: -1])

# # 4 Waga naspisu to suma kodów ascii jego liter. zważ wpisany napis
# c= input()
# suma=0
# for i in c:
#   suma+= ord(i)
# print(suma)

# # 5. policz ile we wepisanym napisie jest liter A.

# e= input()
# ilosc = 0
# for x in e:
#   if x == "A" or "a":
#     ilosc += 1
# print(ilosc)

# #6. Podaj dominującą literke w wpisanym napisie, niech to bedzie tylko jedna literka

# g= input()
# print(g.count("A"))
# max= 0
# for x in g:
#   if g.count(x) > max:
#     max = g.count(x)
#     literka = x 
# print(literka, max)

#8. sprawdz czy w napisie wystepuja trzy podciagi "LA"
h= input()
print("LALALAMALAMA".count("LA"))
for i in range(len(h)):
  if h[ i : i+ 1] :
    ilosc += 1
    if ilosc == 3
    print("TAK")
  else:
    print("NIE")
    