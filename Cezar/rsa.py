#PRE

from math import gcd
print(gcd(20,15))

# 1. wybór dużych liczb pierwszych
p = 11
q= 13
print(p,q)

# 2. Obliczenie q*p=n i funkcji Eulera  F=(p-1)*(q-1)
n = p*q
F = (p-1) * (q-1)
print(n)
print(F)

# 3. Generujem klucz publiczny e taki ze NWD(e,F)=1
from math import gcd
for i in range(2,F):
  if gcd(i,F)== 1:
    e=i
    break
print(e, n)

#4. generujemy klucz prywatny d taki ze d*e mod F = 1
for j in range(2,F):
  if ((j*e) %  F) ==1:
    d=j
    break
print(d,n)

#5. przykład działania rsa
#m - moja wiadomośc
# c = m**e % n (szyfrogram- cypher- wiadomośc zaszyfrowana)
#t = c**d % n (tekst jawny czyli nasza wiadomość -  text(message))

m = input()
cipher= ""

for i in m:
 cipher =+ (chr(ord(i)**e)%n)
print(cipher)

tekst=""
for j in cipher:
  tekst =+ (chr(ord(i)**e)%n)

