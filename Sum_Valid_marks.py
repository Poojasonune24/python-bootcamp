student_list = [100, -1, 200, 300, -1, 400, 500]

students_count =0
Total_marks =0

for student in student_list:
    if student < 0:
        students_count +=1
        continue

    Total_marks = Total_marks +student
    students_count += 1

print("Total Marks = ", Total_marks)
print("Student Count = ",students_count)
