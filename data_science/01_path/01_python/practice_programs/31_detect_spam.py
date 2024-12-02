# problem
# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# solution
spam_strings = ["Make a lot of money", "buy now", "subscribe this", "click this"]

user_comment = input("Please enter your comment: ")

isSpam = user_comment in spam_strings

if isSpam:
    print("Alert, spam detected.")
else:
    print("No spam.")
