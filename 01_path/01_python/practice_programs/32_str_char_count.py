# problem
# Write a program to find whether a given username contains less than 10 characters or not.

# solution
username = input("Please enter you username: ")
username_length = len(username)

if username_length < 10:
    print(f"{username} has less than 10 characters.")
elif username_length == 10:
    print(f"{username} has exactly 10 characters.")
else:
    print(f"{username} has more than 10 characters.")
