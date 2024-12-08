# problem
# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# solution
user_marks = float(input("Enter your marks: "))

if user_marks < 50:
    print(f"Your grade: F")
elif user_marks < 60:
    print(f"Your grade: D")
elif user_marks < 70:
    print(f"Your grade: C")
elif user_marks < 80:
    print(f"Your grade: B")
elif user_marks < 90:
    print(f"Your grade: A")
elif user_marks <= 100:
    print(f"Your grade: Ex")
else:
    print("Invalid marks. Marks must be 1-100.")
