# problem
# Write a program to find the sum of first n natural numbers using while loop.

# solution
n = int(input("Enter n: "))
sum = 0

if n >= 1:
    for i in range(1, n + 1):
        sum += i
        i += 1
    print(sum)
else:
    print("Number mustbe >= 1.")
