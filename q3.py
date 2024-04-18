#3] Write a program to accept three integer numbers and find its average.

# Accept three integer numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))



# Calculate the average
print(f"average of {num1}, {num2}, {num3} is {round(((num1 + num2 + num3) / 3),3)}")
