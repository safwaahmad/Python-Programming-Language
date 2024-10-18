#list
#list are used to store multiple iteems or attribute in single variable or entitiy
#list it can be changeable (MUTABLE)
#store multiple datatype
#nested - list  
#different data-type in same list
##<List is a collection which is ordered and changeable. Allows duplicate members>

example = ["sunady","monday","tuesday"]
print(example)
print("-------------------------------")
dif_data_type =[1,2.9,"safwan",True]
print(dif_data_type)
print(type(dif_data_type))
print(len(dif_data_type))
print("-------------------------------")
nested_list= ["python", [1,2,3], "safwan"]
print(nested_list)
print(type(nested_list))
print(len(nested_list))
print(nested_list[0]) #by indexing
print(nested_list[:3])#by slicing
print(nested_list[0]=="python") 
nested_list[0]="java"
print(nested_list)
print(nested_list[0]=="python") 
print(dif_data_type[0:3:1]) # 1 is the space b/w 0:3
dif_data_type.append(5) #in last
print(dif_data_type.append)
print("------Python - Change List Items------")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
thislist.insert(0, "watermelon")
print(thislist)
print("------Python - Add List ------")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") ##--------------Append Items
print(thislist)
#--The insert() method inserts an item at the specified index:
print("----Insert Items----")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") ##-----------Insert Items
print(thislist)
#To append elements from another list to the current list, use the extend() method.
print("-----Extend List-----")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  ##-----------Extend list
print(thislist)
print("---------REMOVE-------")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  ##Remove Specified Index
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]  ##delete the list
print(thislist)
print("-------------------------------")
#add string to list
name = "safwan"  #string 
print(list(name)) #list
line=["a",1,"b",2]#list
print(list(name)+line) # concatinating two list

str = "Hello"
print(id(str))
