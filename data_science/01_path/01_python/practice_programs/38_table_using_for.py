# problem
# Write a program to print multiplication table of a given number using for loop.

# solution
number = int(input("Enter a number you want to print table of: "))

for i in range(1, 11):
    print(f"{number} * {i} =  {number * i}")
    i += 1
