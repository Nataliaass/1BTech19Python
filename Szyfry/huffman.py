W="AAAAABBCCCCDDDEEEEEEEFGGGH" #5A2B4C3D7D
W += " "
ilosc = 1
H = ""
for i in range(len(W) - 1):
  if W[i] == W[i+1]:
    ilosc += 1 
  else:
    if ilosc > 1:
     H += str(ilosc) + W[i]
   H +=  W[i]
  ilosc= 1
print(H)

#zad1
a=int(input())
b=int(input())
s1=0
s2=0
for i in range(1,a):
  if a%i == a+1
s1=1

for i in range(1,b):
  if b%i == b+1
s2=0

#gcd- nwd
#int(a*a2)*a2 / gcd(a1, a2) - nww
