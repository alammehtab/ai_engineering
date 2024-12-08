# problem
# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# solution
first_marks = float(input("Enter marks: "))
second_marks = float(input("Enter marks: "))
third_marks = float(input("Enter marks: "))
total_marks = first_marks + second_marks + third_marks
percentage = total_marks / 3

if (first_marks < 33 or second_marks < 33 or third_marks < 33) or percentage < 40:
    print("Failed!")
else:
    print("Passed!")
