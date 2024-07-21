#implicit typecasting
#explicit typecasting
x=10
y=15
c= "5"
d= "9"
print(x+y)
print(c+d)
print(type(x))
print(type(y))
print(int(x)+int(y))
print(type(x))
print(type(y))
print(int(c)+int(d))

#----------------------------
#----Type Casting------------
a="123"            #datatype string 
print(type(a),a) 
a= int(a)          #changign datatype string to int
print(type(a),a)   #datatype int
print(type(a+3),a+3)
print("----------------------------")
a=123
print(type(a),a)
a= str(a)
print(type(a),a)

print("---------altarnativee-------")
print(type(str(21.9)))    #float to string
print(type(float("21")))  #string to float
print(type(int("21")))    #string to int
print(type(int(21.9)))    #float to int 

#??//kal ham na local computer pr hi add kiya tah  or create directory ki thi us sa yani 
# git hub mn to koi changev nhi aya tah naw?