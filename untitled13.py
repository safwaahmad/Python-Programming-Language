
name = "ahmad"
age = "30"
str ="my name is {} of age {}"

print(str.format(name,age))

print(len(str))

a= "university"
print((a.upper()),a)

x = " BELONG TO FSD"

#if "BELONG" in x
print("yes , it is presnt")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("Hello"))
print(bool(15))
print(bool(10<4))

x = 9
x%=2
print(x)

thislist = [ "cherry", "apple","apple", "banana"]
print(type(thislist))
print(len(thislist), thislist)

list1 = ["apple","banana"]
list2 = [1,2,3,4,5]
list3 = [True, False]
list4 =[1, 2, 'apple', 4]
print(list4)
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist[-1])
#print("apple" in list4)/
if "apple" in list4:
  print("Apple is present")

#
list1 = ["apple","banana"]
list1[0:1]=["cherry"]
print(list1)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# to insert value in array
list = ["apple", "banana", "cherry"]
list.insert(2, "watermelon")
print(list)
thislist1 = ["apple", "banana", "cherry"]
thislist1.append("orange")
print(thislist1)
thislist2 = ["apple", "banana", "cherry"]
thislist2.extend("tropical")
print(thislist2)
thislist3 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist3.extend(thistuple)
print(thislist3)

