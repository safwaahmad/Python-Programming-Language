



a= 1
b="2"
c=2.3
d=9.45667
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)

x="8"
print(type(x),x)
x=float(x)
print(type(x),x)

for x in "banana":

  print(x)
  y=7

  print(x,y)

x = "HELLO,WORLD"
print(type(len(x)),x)

txt = "The best things in life are free!"
print("frees" in txt)



str = "Present the name safwan"
if "ahmad" not in str:
 print("yes , safwan  is presnt ")

x = "  hello, world !"
#print(x[-5:-3])
print(x.upper())
print(x.lower())
print(x.strip())
print(x.replace("h","E"))
print(x.split(","))

from os import fchdir
a = "Hello"
b = "World"
c = a +" "+ b
x= 8
y=10
e= "12"
f="13"
e = int(e)
f = int(f)

print(e)
print(f)
g=e+f

d=x+y

print(g)
print(d)
print(c)

age = "36"
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
name =  "safwan"
str =  " ahamad"
price = 786
quantity= 55
info = "my name is {} with name {} having money {} of quantity  {} "
print(info.format(name,str,price,quantity))

x = 'hello'
print(x[2])