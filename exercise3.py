meal=int(input("Enter the meal price: "))
tip=int(input("Enter the tip percentage: "))
ppl=int(input("Enter the number of people: "))
eachperson=meal+(meal*tip/100)/ppl
print("Each person pays: "+str(round(eachperson,2))+" RMB")

