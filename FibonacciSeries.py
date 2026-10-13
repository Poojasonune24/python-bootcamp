
n=int(input("Enter number : "))
first_number = 0
Second_number =1
print(first_number)
print(Second_number)

for i in range (n-2):

    number = first_number+Second_number
    print(number)
    first_number = Second_number
    Second_number = number
