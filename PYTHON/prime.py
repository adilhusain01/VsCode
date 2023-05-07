#prime numbers without using functions
flag=0
x=int(input("Enter a number: "))
if (x<=1):
    print("Not Prime")
else:
    for i in range(2,x):
        if x%i==0:
            flag=1
            break
    if flag==0:
        print("Prime")
    else:
        print("Not Prime")