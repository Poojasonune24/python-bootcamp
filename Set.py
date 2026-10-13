Students_list = {"sam", "john", "ram", "sid"}

list_of_student = ["sid","yug", "sonam", "ram"]

for student  in list_of_student:
    
    if student in Students_list:
        print(Students_list)
    else:
        Students_list.add(student)
        print(Students_list)