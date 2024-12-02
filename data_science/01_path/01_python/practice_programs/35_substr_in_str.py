# problem
# Write a program to find out whether a given post is talking about “Harry” or not.

# solution
wanted_string = "Harry"
post = "this is the story of Jerry Potter. He was an excellent student."

if wanted_string in post:
    print("Yes it does.")
else:
    print("No it does not.")
