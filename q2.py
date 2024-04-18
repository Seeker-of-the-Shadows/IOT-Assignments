# 2] Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values

number=int(input("give a number"))


def face_value(n):
    print("face value of each decimal digit")
    
    a=4
    while a>0:
        print((number//int(power10(a)))%10,end=" ")
        a-=1

def place_value(n):
    print("\nplace value of each decimal digit")
    
    a=4
    while a>0:
        print((number//int(power10(a)))%10*(int(power10(a))),end=" ")
        a-=1

def rev(n):
    print("\n reverse order")
    
    a=1
    while a<5:
        print((number//int(power10(a)))%10,end=" ")
        a+=1

def power10(n):
    a=1
    while n>1:
        
        a=a*10
        n=n-1
    return a

face_value(number)
place_value(number)
rev(number)