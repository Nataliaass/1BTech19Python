#palindrom za pomoca tablicy
s= input()
for i in range(len(s)//2):
  if s[i] != s[len(s)-1-i]:
    exit("nie jest")
exit("jest palindromem")

#anagram za pomoca tablicy
#anagram za pomoca funkcji
a = input()
b = input()
A=list(a)
B=list(b)
A.sort()
B.sort()

a= "".join(A)
b= "".join(B)
print(a, b)
if a==b:
  print("Tak")
else:
  print("Nie")
