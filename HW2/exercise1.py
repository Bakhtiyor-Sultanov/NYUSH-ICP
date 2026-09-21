table=str(input("Is a table available? Yes/No?: "))
table=table.upper()

if table=="YES":
    pass
else:
    print("No")
people=int(input("How many people?: "))
if people <= 6:
    print("Reservation confirmed. A regular table has been reserved")
elif people > 6:
    print("Reservation confirmed. A large table has been reserved")

    
