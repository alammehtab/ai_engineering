# problem
# Replace the double spaces with single space.

# solution
user_input = input("Please enter a string: ")

if user_input.find("  ") != -1:
    user_input = user_input.replace("  ", " ")

print(user_input)
