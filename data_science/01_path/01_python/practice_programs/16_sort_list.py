# problem
# Write a program to accept marks of 6 students and display them in a sorted manner.

# solution
student_marks = []

m1 = float(input("Enter marks1: "))
student_marks.append(m1)

m2 = float(input("Enter marks2: "))
student_marks.append(m2)

m3 = float(input("Enter marks3: "))
student_marks.append(m3)

m4 = float(input("Enter marks4: "))
student_marks.append(m4)

m5 = float(input("Enter marks5: "))
student_marks.append(m5)

m6 = float(input("Enter marks6: "))
student_marks.append(m6)

student_marks.sort()

print(student_marks)
