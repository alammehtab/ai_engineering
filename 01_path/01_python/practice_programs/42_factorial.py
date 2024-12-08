# problem
# Write a program to calculate the factorial of a given number using for loop.

# solution
number = int(input("Enter a number: "))
factorial = 1

if number < 0:
    print(f"{number} is not valid for factorial.")
elif number == 0 or number == 1:
    print(f"Factorial of {number}: {1}")
else:
    for i in range(2, number + 1):
        factorial *= i
        i += 1
    print(f"Factorial of {number}: {factorial}")
