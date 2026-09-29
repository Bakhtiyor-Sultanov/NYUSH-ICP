score=int(input("Type the score: "))

while score >= 100 or score <=0:
    print("Invalid input. Please enter a score between 0 and 100.")
    score=int(input("Type the score: "))
if score <= 100 and score >=0:
    if score < 63:
        print("F")
    if score >=63 and score < 67:
        print("D")
    if score >=67 and score < 70:
        print("D+")
    if score >=70 and score < 73:
        print("C-")
    if score >=73 and score < 77:
        print("C")
    if score >=77 and score < 80:
        print("C+")
    if score >=80 and score < 83:
        print("B-")
    if score >=83 and score < 87:
        print("B")
    if score >=87 and score < 90:
        print("B+")
    if score >=90 and score < 95:
        print("A-")
    if score >= 95:
        print("A")
