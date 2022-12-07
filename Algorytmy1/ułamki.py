a= int(input())
b=int(input())
c=int(input())
d=int(input())

x, y= b, d
iloczyn = x*y
while y> 0:
  x, y = y, x% y
nww= iloczyn // x
e= (nww //b) * a
f=(nww //d) * c
print(f"{a}/{b}+ {c}/{d} = {e}/{nww} + {f}/{nww} = {f+e}/{nww}")
