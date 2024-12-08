# problem
# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry","Soham","Sachin","Rahul"]

# solution
l = ["Harry", "Soham", "Sachin", "Rahul"]

# using for loop
# for user in l:
#     if user[0] == "S":
#         print(f"Helloooo, {user}")

# using while loop
i = 0
while i < len(l):
    if l[i][0] == "S":
        print(f"Helloooo, {l[i]}")
    i += 1
