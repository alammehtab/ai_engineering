# problem
# Write a recursive function to calculate the sum of first n natural numbers.


# solution
def calculate_sum(n):
    i = n
    sum = 0
    while i > 0:
        sum += i
        i -= 1

    return sum


print(calculate_sum(5))
