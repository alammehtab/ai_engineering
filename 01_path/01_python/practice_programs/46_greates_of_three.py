# problem
# Write a program using functions to find greatest of three numbers.


# solution
def greates_of_three(a, b, c):
    if a > b and a > c:
        print(f"Greatest number is: {a}")
    elif b > c:
        print(f"Greatest number is: {b}")
    else:
        print(f"Greates number is: {c}")


greates_of_three(11, 21, 3)
