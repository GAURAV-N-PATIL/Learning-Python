# Mini project : student marks calculator


def grade():
    total_marks=Marks_Maths_2 + Marks_Statistics_1 + Marks_Python + Marks_English_2
    average_marks=total_marks / 4
    if average_marks >= 90:
        print("Grade: S")
    elif average_marks >= 80:
        print("Grade: A")
    elif average_marks >= 70:
        print("Grade: B")
    elif average_marks >= 60:
        print("Grade: C")
    else:
        print("Grade: F")
def percentage():
    total_Percentage=(Marks_Maths_2 + Marks_Statistics_1 + Marks_Python + Marks_English_2) / 400 * 100
    print("Total Percentage: ", total_Percentage, "%")
    Maths_percentage=(Marks_Maths_2 / 100) * 100
    Statistics_percentage=(Marks_Statistics_1 / 100) * 100
    Python_percentage=(Marks_Python / 100) * 100
    English_percentage=(Marks_English_2 / 100) * 100
    print("Maths Percentage: ", Maths_percentage, "%")
    print("Statistics Percentage: ", Statistics_percentage, "%" )
    print("Python Percentage: ", Python_percentage, "%")
    print("English Percentage: ", English_percentage, "%")
# main function:
print("Welcome to student Marks Calculator!")
print("Enter Marks for Each subjects:")
Marks_Maths_2=int(input("Maths: "))
Marks_Statistics_1=int(input("Statistics: "))
Marks_Python=int(input("Python: "))
Marks_English_2=int(input("English: "))
Choice=int(input("Enter 1 to calculate Grade or 2 to calculate Percentage: "))
match Choice:
    case 1:
        grade()
    case 2:
        percentage()
    case _:
        print("Invalid Choice! Please enter 1 or 2.")
