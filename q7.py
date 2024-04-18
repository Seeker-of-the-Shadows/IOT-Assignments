#7) Using for loop, write and run a Python program to find factorial from 0 to 10.


# Function to calculate factorial
def facto(n):
    f = 1
    for i in range(1, n + 1):
        f *= i

    return f

# Loop to find factorial of numbers from 0 to 10
for i in range(11):
    print(f"The factorial of {i} is {facto(i)}")
