# problem
# Write a program to detect double space in a string.

# solution
user_input = input("Please enter a string: ")

if user_input.find("  ") != -1:
    print("Double space found.")
else:
    print("Double space NOT found.")
