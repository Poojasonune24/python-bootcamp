def Library_policy_update(BookType, Days, Membership):
    Charges = 0
    if BookType == "StandardBook":
        if Days>5:
            Charges = 5*5 + ((Days-5)*10)
        else:
            Charges = Days*5
    elif BookType == "Reference Book":
        if Days>5:
            Charges = 5*5 + (Days-5)*20
        else:
            Charges = 5*5
    if Membership == True:
        Charges = Charges - ((Charges*20)/100)
    return Charges
book = "Reference Book"
Days = 6
Membership = True

Total_bill = Library_policy_update(book, Days, Membership)
print("Your Total bill is : ",Total_bill)



