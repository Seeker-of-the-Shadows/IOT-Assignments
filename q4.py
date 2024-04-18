#4] Write a Python function to find the maximum of three numbers.
def max():
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
    

num1, num2, num3= (input("Enter three numbers separated by space: ").split())
print("Maximum number is:", max())