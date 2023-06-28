#tuple is immutable, support multiple same values
# if it has only one element, you have  to put a comma at the end 
#otherwise it will take that as a string not a tuple


t1=(1,1,2,3,4,5)
#print(t1,"\n")


#count -> we can count the amount of same values 

print(t1.count(1),"\n")


# .index(value)

print(t1.index(5),"\n")

t2 = "Adil","Husain",20,10,2005

# breaking down each element into pieces 


a,b,c,d,e = t2
print("a : ",a,"\n")


g,*h,i = t2
print("g : ",g,"\n")
print("h : ",h,"\n")
print("i : ",i,"\n")