meal=int(input("Enter the meal price: "))
tip=int(input("Enter the tip percentage: "))
ppl=int(input("Enter the number of people: "))
eachperson= (meal+meal*tip/100)/ppl
print(f"Each person pays: {eachperson:.2f} RMB")

