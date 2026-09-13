first_grade=int(input("1st grade (int between 0 and 100):"))
second_grade=int(input("2nd grade (int between 0 and 100):"))
third_grade=int(input("3srd grade (int between 0 and 100):"))

if all(0 <= n <= 100 for n in (first_grade, second_grade, third_grade)):
    print("Avarege grade: ", (first_grade + second_grade + third_grade)/3)
else:
    print(ValueError)
