Grosery_items = {"Milk" : 60, "Bread": 30 ,"Apple":150 ,"Soyabean":40, "Oil": 160}

Out_Of_stock = ["Milk","Bread"]

Order_List = ["Milk","Apple","Oil", "Bread"]

Total_bill = 0
for order in Order_List:
    if order in Out_Of_stock:
        print(order ,"is unavailable")
    else:
        Total_bill = Grosery_items[order] + Total_bill
print(Total_bill)

