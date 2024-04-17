# 2] Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values

number=int(input("give a number"))

# a
def face_value(n):
    print("face value of each decimal digit")
    for a in range(4,0,-1):
        print(number//int(power10(a)),end=" ")
# print(number//1000,end=" ")
# print((number//100)%10,end=" ")
# print((number//10)%10,end=" ")
# print(number%10,end=" ")



# b
print("\nplace value of each decimal digit")
print(number ,end=" = ")
print((number//1000)*1000,end="+")
print(((number//100)%10)*100,end="+")
print(((number//10)%10)*10,end="+")
print((number%10)*1,end=" ")

# c
print("\nreverse order")
print(number%10,end=" ")
print((number//10)%10,end=" ")
print((number//100)%10,end=" ")
print(number//1000,end=" ")

def power10(n):
    a=1
    while n>0:
        
        a=a*10
        n=n-1
    print(a)

face_value(number)

