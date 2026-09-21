year=int(input("Enter the year: "))
leap=False
wc=False
eu=False
print(f"Year:{year}")
if year%4==0 or year%400==0:
    leap=True
if year%100==0:
    leap=False

if leap==True:
    print("Leap year")
else:
    print("Not leap year")

if year >= 1950 and (year-1950)%4==0:
    wc=True
    print("World Cup year")
else:
    wc=False
    
if year >= 1960 and (year-1960)%4==0:
    eu=True
    print("Euro Cup year")
else:
    eu=False

    