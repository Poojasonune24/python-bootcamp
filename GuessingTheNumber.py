import random

computer_number = random.randint(1, 5)
print("Welcome to Interesting Game - Guess the number in 3 attempt")

Attempt = 1
for i in range(1,4):
    number = int(input("Guess the number: "))
    if computer_number == number:
        print("You win, Congrats!!")
        break
    else:
        if Attempt == 3:
            print("Attempt over, Good luck next time")
        else:
            print("Wrong guess, attempt again")
            Attempt += 1
            

