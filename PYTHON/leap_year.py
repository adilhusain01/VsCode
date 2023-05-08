#Program to check leap year using functions

def isleap(n):
    if (n>0):
        if ((n%100==0)and(n%400==0)) or ((n%4==0)and(n%100!=0)):
            return "Its a leap year"
        else:
            return "Its not a leap year"
    else:
        return "Not a valid input"

year=int(input("Enter a year: "))
print(isleap(year)) 