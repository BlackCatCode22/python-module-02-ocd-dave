def show_message(num1, num2, num3, largest, largest_var):
    print(f"You entered three numbers: {num1}, {num2}, and {num3}.")
    print(f"num1 = {num1}, num2 = {num2}, num3 = {num3}.")
    print(f"The largest number is {largest}, and it was stored in {largest_var}.")

num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
num3 = int(input("enter third number "))

if num1 >= num2 and num1 >= num3:
    largest = num1
    largest_var = "num1"
elif num2 >= num1 and num2 >= num3:
    largest = num2
    largest_var = "num2"
else:
    largest = num3
    largest_var = "num3"

show_message(num1, num2, num3, largest, largest_var)
