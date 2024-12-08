# problem
# Write a program to find whether a given number is prime or not.

# solution
number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is NOT PRIME.")
            break
    else:
        print(f"{number} is PRIME.")
else:
    print(f"{number} is NOT PRIME.")
