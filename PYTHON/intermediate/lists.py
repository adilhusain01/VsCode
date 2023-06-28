#Lists : ordered, mutable, allows duplicate elements



'''
l1 = ["a","b","c"]
print("Original list is :. ",l1,"\n")

#len(...) -> gives length of the list

print(len(l1))

# .append(...) to the list

l1.append("d")
print("'d' Appended list is : ",l1,"\n")

# .pop()

l1.pop()
print("Popped list is : ",l1,"\n")

# .insert(index, value)

l1.insert(0,"z")
print("'z' Inserted at 0 : ",l1,"\n")

# ...remove(value)
l1.remove("z")
print("After removing 'z' : ",l1,"\n")

# .sort(...)

l1.sort()
print("The sorted list : ",l1,"\n")

# .revserse()

l1.reverse()
print("The reversed list is : ",l1,"\n")


#  sorted(list) to put items in the new list

l2=sorted(l1)
print("This is the l2 sorted list of l1: ",l2,"\n")

# .clear()

l1.clear()
print("The cleared list is : ",l1,"\n")
'''


#multipying elements of the list

'''
l3=[1,2,3,4,5]*5
print("Multiplied list by 5 : ",l3,"\n")

#addind two lists

l3=l3[0:5]
l4=[6,7,8,9]
l5=l3+l4
print("Added two lists : ",l5,"\n")

#slicing

print("Gap of one btw each element by slicing: ",l5[::2],"\n")

print("Reversed  list by slicing : ",l5[::-1],"\n")

#copying list

list1 = [1,2,3,4,5]
list2 = list1

print("List 2 as copy of list 1 : ",list2,"\n")
list2.append(6)

print("Shows that we can modify list1 through list2 : ",list1,"\n")
'''

#########   this can be prevented by using the .copy_function/slicing method/or list function

# .copy() function

'''
list2=list1.copy()
print("Copied list2 using copy fnc now : ",list2,"\n")

list2.append(7)
print("Shows that now list2 cant modify list1 : ",list1,"\n")
'''


#list method

'''
list2=list(list1)
print("list2 using list method : ",list2,"\n")

list2.append(7)
print("Shows that list2 is actually a copy of list1 : ",list1,"\n")
'''


#slicing method

'''
list2=list1[:]
print("copy of list1 using slicing : ",list2,"\n")

list2.append(7)
print("Shows that now list2 cant modify list1 : ",list1,"\n")
'''



# i for i method
'''
a=[1,2,3,4,5,6]
b=[i*i for i in a]
print("list of square of each element of a : ",b,"\n")
'''