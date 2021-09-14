def Input():
    print("Enter three grades.")
    grade1 = int(input())
    grade2 = int(input())
    grade3 = int(input())
    Average(grade1, grade2, grade3)

def Average(grade1, grade2, grade3):
    sum = grade1 + grade2 + grade3
    avg = sum/3
    Output(avg)

def Output(avg):
    print("Average =", avg)
