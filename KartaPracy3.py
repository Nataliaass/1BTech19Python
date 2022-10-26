
for i in range(3, 10):
    print(i)

for i in range(10, 22):
    print(i, end=" ")
  
for i in range(15,33,2):
     print(i)

for i in range(99,9,-1):
  print(i, end= " ")

for i in range(60,10):
  print(i)

for i in range(100,1000,20):
  print(i, end=" ")

print()
print()
for i in range(5,50):
  print(i*20, end=" ")
  
#Zad 1
  n= int(input())
  
for i in range(n):
  print(i**3 + 3, end=" ")
#zad2
for i in range(105,1000,15):
  if i % 15 == 0 :
  print(i, end=" ")

#zad3
p=int(input())
print("Podaj liczbę:" ,)


#zad 5
n=int(input(" w ile gramy:"))

suma= n* (n+1) // 2
print(suma)
a=int(input())

for i in range(n-1) :
  a= int(input()) 
  suma= suma - a
print(suma)

#zadanie napisz pętle sumującą liczby dwucyfrowe parzyste

suma=0
for i in range(10,100,2):
      suma= suma + n
print(suma)  