# Get three integers from the user
print("Get three integers from the user and find the largest of the three")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Use nested if statements to find the largest
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

# Output the result
print("The largest of 3 is:", largest)