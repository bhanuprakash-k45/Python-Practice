items=["Bru","Sugar","Milk"]#list
print(items)
print(items[0])#list in index
print(items[-1])#list in index
#modify list
items.pop()
items.append("Biscuit")#adding new item in list
print(items)
items.remove("Sugar")#remove item from list
print(items)
items.insert(1,"Egg")#insert item via index element
print(items)
items[1]="Butter"#modify/replace item via index element
print(items)
items.clear()#clear all items from list
print(items)

#slicing lists
numbers=[0,1,2,3,4,5,6]
print(numbers[1:5])#slicing list from index 1 to 4
print(numbers[:3])
print(numbers[::2])

#list functions and methods
print(len(numbers))#length of list
numbers=[5,2,9,1]
print(sorted(numbers))#sort list in ascending order
print(numbers)
print(sum(numbers))#sum of list

#Methods
print(items.index("Bru"))#index of item in list
numbers=[1,2,3,1,1]
print(numbers.count(1))#count of item in list
items.reverse()#reverse the list
print(items)
numbers.sort()#sort the list in ascending order
print(numbers)

#Nested lists
m=[[1,2],[3,4]]
print(m[0])
print(m[1][1])#accessing nested list