#jak wydobyć ostatnie 2 cyfry z liczby?
n=12345
print ((n%1000))

#pierwiastek
from math import sqrt
print(sqrt(576))

#2
#liczba 3cyfrowa podzielna przez 13 i nie podzielna pzrez 4
for i in range(100,1000):
  if i % 13 == 0 and i % 4 != 0:
    print(i, end=" ")

n=24
suma=0
ilosc=0
for i in range(1,25):
  if n% i ==0:
    print(i)
         suma = suma + i
         ilosc=ilosc +1
print("suma",suma)
print("ilosc",ilosc)

#oblicz sume k poczatkowych liczb trzycyfrowych
#100+101+102+103
#we:4
#wy: 406
k=4
suma=0
ilosc=0
for i in range(100,1000):
  suma= suma+ i
  ilosc=ilosc+1
  if ilosc ==k:
    break
print(suma)


k=4
suma=0
for i in range(100,1000+k):
  suma= suma+i


n= int(input())
a, b= 0, 1
suma=0
for i in range(n):
  a, b= b, a+b
  suma=suma +b
print(suma)

