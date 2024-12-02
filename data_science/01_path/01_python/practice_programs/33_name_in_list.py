# problem
# Write a program which finds out whether a given name is present in a list or not.

# solution
names = ["ali", "bilal", "danyal"]
user_name = input("Enter your name: ")

isFound = user_name in names

if isFound:
    print("User found.")
else:
    print("User not found.")
