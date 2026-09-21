table=str(input("Is a table available? (yes or no):"))
table=table.upper()
people=0
if table=="NO":
    print("Sorry, the restaurant is fully booked.")
if table=="YES":
    people=int(input("How many people?: "))
    if people <= 6:
        print("Reservation confirmed. A regular table has been reserved.")
    elif people > 6:
        print("Reservation confirmed. A large table has been reserved.")



    
