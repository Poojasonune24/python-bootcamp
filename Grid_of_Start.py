Number_Of_star = int(input("Enter the number of the stars: "))

star = Number_Of_star

for i in range(Number_Of_star):

    for S in range(star):
        print("* ",end = "")
    print()
    
    star = star - 1