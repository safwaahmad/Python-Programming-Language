#list
#list are used to store multiple iteems or attribute in single variable or entitiy
#list it can be changeable (MUTABLE)
#store multiple datatype
#nested - list  
#different data-type in same list


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
print("-------------------------------")
#add string to list
name = "safwan"  #string 
print(list(name)) #list
line=["a",1,"b",2]#list
print(list(name)+line) # concatinating two list

str = "Hello"
print(id(str))
