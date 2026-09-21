sqr=input("Enter a chess board position: ")
columns = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}
letter=int(columns[sqr[0]])
num=int(sqr[1])

color_num=letter+num
if color_num%2==0:
    print("Black")
if color_num%2==1:
    print("White")